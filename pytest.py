from ilsmc.optimizer import trans_emiss_calc
import pandas as pd
import sys
import numpy as np
from ilsmc.optimizer import optimizer_lipo
from ilsmc.optimizer import forward_loglik
from ilsmc.optimizer import write_list


seed = int(sys.argv[1])
n_int_AB = int(sys.argv[2])
n_int_ABC = int(sys.argv[3])

t_1 = 2e5
t_2 = 4e4
t_upper = 5e5 
N_AB = 30000
N_ABC = 40000
r = 1e-8
mu = 2e-8


transitions, emissions, starting, hidden_states, observed_states = trans_emiss_calc(
    t_1, t_2, t_upper, 
    N_AB, N_ABC, 
    r, mu, n_int_AB, n_int_ABC)


np.random.seed(seed)

n_sim = 100000
H = np.zeros(n_sim, dtype = np.int16)
E = np.zeros(n_sim, dtype = np.int16)
h = np.random.choice(
    list(range(len(hidden_states))),
    p = list(starting)
)
H[0] = h
e = np.random.choice(
    list(range(len(observed_states))),
    p = emissions[H[0]]
)
E[0] = e

for i in range(1, n_sim):
    h = np.random.choice(
        list(range(len(hidden_states))),
        p = transitions[H[i-1]]
    )
    e = np.random.choice(
        list(range(len(observed_states))),
        p = emissions[h]
    )
    E[i] = e
    H[i] = h



write_list([-1, t_1, t_2, t_upper, N_AB, N_ABC, r, mu, forward_loglik(transitions, emissions, starting, E)], 'results/tab_{}_{}_{}'.format(seed, n_int_AB, n_int_ABC))


res, y = optimizer_lipo(n_int_AB, n_int_ABC, E, 'results/tab_{}_{}_{}'.format(seed, n_int_AB, n_int_ABC))




