from gwf import Workflow

gwf = Workflow()

for i in range(10):

    gwf.target('TestRun_{}'.format(i), 
               inputs=[], 
               outputs=['results/tab_{}.csv'.format(i)],  
               cores=3,
               memory='12g',
               walltime= '03:00:00',
               account='Primategenomes') << """
    python pytest.py {}
    """.format(i)


for i in range(10, 20):

    gwf.target('TestRun_{}'.format(i),
               inputs=[],
               outputs=['results/tab_{}.csv'.format(i)],
               cores=3,
               memory='12g',
               walltime= '06:00:00',
               account='Primategenomes') << """
    python pytest_n3.py {}
    """.format(i)
