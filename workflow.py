from gwf import Workflow

gwf = Workflow()


for n in range(1, 4):
    for i in range(10):

        gwf.target('TestRun_{}_{}_{}'.format(i, n, n), 
                   inputs=[], 
                   outputs=['results/tab_{}_{}_{}.csv'.format(i, n, n)],  
                   cores=3,
                   memory='50g',
                   walltime= '12:00:00',
                   account='Primategenomes') << """
        python pytest.py {} {} {}
        """.format(i, n, n)




# for i in range(10, 20):
#     gwf.target('TestRun_{}'.format(i),
#                inputs=[],
#                outputs=['results/tab_{}.csv'.format(i)],
#                cores=3,
#                memory='36g',
#                walltime= '12:00:00',
#                account='Primategenomes') << """
#     python pytest_n3.py {}
#     """.format(i)
