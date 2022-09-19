import multiprocess as mp
import os

print(mp.cpu_count())

print(int(os.environ["SLURM_JOB_CPUS_PER_NODE"]))

print(int(os.environ['SLURM_CPUS_PER_TASK']))

print(len(os.sched_getaffinity(0)))
