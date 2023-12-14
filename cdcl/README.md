This directory implements various methods for parallelizing CDCL. 

The folder 'hordesat-src' implements the CDCL algorithm utilizing the parallel SAT solver portfolio (implementing parallelism via OpenMPI) for the CDCL algorithm. Information about the HordeSAT portfolio can be found in the paper https://algo2.iti.kit.edu/balyo/papers/horde.pdf

The files sequential_cdcl.cpp and openmp_cdcl.cpp implement cpp versions of the algorithm, where parallelism is implemented using OpenMP.
