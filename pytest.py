from ilsmc.optimizer import trans_emiss_calc
import pandas as pd
import sys
import numpy as np
from ilsmc.optimizer import optimizer
from ilsmc.optimizer import forward_loglik
from ilsmc.optimizer import write_list


seed = int(sys.argv[1])


transitions, emissions, starting, hidden_states, observed_states = trans_emiss_calc(
    t_1 = 2e5, t_2 = 5e4, t_upper = 2e5,     
    N_AB = 50000, N_ABC = 60000, 
    r = 1e-8, mu = 5e-9, n_int_AB = 1, n_int_ABC = 1)


np.random.seed(seed)

n_sim = 1000000
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

t_init = 1e5
N_init = 70000
r_init = 5e-8
mu_init = 1e-9


write_list([-1, 2e5, 5e4, 2e5, 50000, 60000, 1e-8, 5e-9, forward_loglik(transitions, emissions, starting, E)], 'results/tab_{}'.format(seed))

res = optimizer(t_init, t_init, t_init, 
                N_init, N_init, 
                r_init, mu_init, 
                1, 1, E, 'results/tab_{}'.format(seed))


