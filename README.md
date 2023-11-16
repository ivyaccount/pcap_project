# Parallel Strategies for SAT Solver Optimization: A Comparative Study

## TEAM MEMBERS:
 Yi-Ju Huang (yijuh), Raashi Mohan (raashim)

## SUMMARY:

We aim to compare various SAT (Satisfiability) solver algorithms and determine their parallel implementation potential. By leveraging different parallel strategies, such as OpenMP and OpenMPI on CPUs, we intend to analyze and contrast the efficiency of parallelizing different SAT solver strategies, and see which strategies can take the most advantage of parallelism.

## BACKGROUND:

_What is the SAT problem?_

Boolean satisfiability problem (SAT problem) is a problem to determine whether a set of boolean expressions is satisfiable. It is the first problem proved to be NP-complete in the Computer Science field that has been studied for decades.

_How do people solve it?_

With the long study, there are several algorithms that are developed to solve the problem efficiently. The naive approach using brute force is listing all the possibilities with booleans to check if expressions are satisfiable. Modern techniques use smarter ways to refine the scope. Davis-Putnam-Logemann-Loveland algorithm (DPLL) uses backtracking techniques, conflict-driven clause learning (CDCL) adopts DPLL but backtracks non-chronologically, while stochastic local search algorithms such as WalkSAT and GSAT incorporate randomness in their search process.

_How can we leverage parallelism to the SAT solvers?_

With the abundance of choice, we are wondering which algorithm can leverage parallelism the most. With this information, future users may take advantage of their own platform to achieve the best.

## THE CHALLENGE:

Parallelizing SAT solver algorithms poses several challenges due to the nature of the SAT solving process itself. The key difficulties in parallelizing SAT solver algorithms revolve around the inherent sequential nature of certain steps within these solvers and the complex dependencies between decision-making and clause evaluations. There are several considerations to make when constructing our implementations:



1. **Dependencies**: These types of algorithms rely heavily on decision-making and clause propagation. Dependencies arise from the decisions made at each step and have the ability to influence subsequent steps. Branching decisions lead to a complex web of dependencies, as well as divergent execution paths, - managing these branches in a parallel environment requires synchronization and careful handling to maintain correctness and avoid redundant work. Additionally, coordinating these parallel threads to ensure consistent decision-making and backtracking without compromising correctness will prove to be complex.
2. **Memory Access Characteristics**: SAT solvers involve evaluating clauses against assignments, which results in frequent memory accesses to store and retrieve clause data. When considering an implementation, it is vital to ensure that necessary memory accesses exhibit strong locality, to eliminate cache misses and memory contention whenever possible.
3. **Communication to Computation Ratio**: As mentioned before, SAT solving involves significant computation in the form of clause evaluations, decision branching, and backtracking. However, in a parallel context, the need for synchronization and communication between threads for sharing information, managing decision states, and handling conflicts can increase the communication overhead compared to these computational tasks. This imbalance can impact the scalability of parallel SAT solvers.
4. **Resource Contention**: For certain approaches, shared resources like memory, data structures, and caches can become bottlenecks in parallel SAT solvers. Managing concurrent access to these shared resources without causing contention or excessive synchronization overhead is a constraint that needs careful consideration.

## RESOURCES:

**GHC Machine**

Intel Core i7-9700 processor (3.0 GHz , Eight cores, 8 threads)

**Pittsburgh Super Computer**

CPU: AMD EPYC 7742 (2.25-3.40 GHz, 64 cores, 128 threads)

**Preliminary Code Base**

We will refer to the code bases below as starting points for optimization.

DPLL: [https://github.com/uzum/dpll-sat-solver/tree/master](https://github.com/uzum/dpll-sat-solver/tree/master)

CDCL: [https://github.com/sukrutrao/SAT-Solver-CDCL](https://github.com/sukrutrao/SAT-Solver-CDCL)

WalkSAT: [https://github.com/Shahriar9000/Optimized-WalkSat-and-Resolution-Proving](https://github.com/Shahriar9000/Optimized-WalkSat-and-Resolution-Proving)

**Paper reference**



* Optimizing stochastic local search algorithms: TBD

## GOALS AND DELIVERABLES:

**Plan to Achieve:**



* Implement sequential, single-thread versions of the following SAT solver algorithms: brute force, DPLL, CDCL
* Implement CPU-based parallelized versions of these algorithms. 
* Perform a comprehensive analysis and comparison of the implemented methods, including evaluations on performance, scalability, and different types of costs

**Hope to Achieve:**



* Implement sequential and CPU-based parallelized versions of the WalkSAT algorithm
* Implement parallel implementations that use CUDA on GPUs.

**Deliverables:**



* Display a multitude of graphs showcasing the performance improvements achieved through parallelization, as well as other metrics compiled (such as scalability and proportions of different types of computational cost).
* Present a comparative analysis report summarizing the strengths and weaknesses of each parallel implementation.

## PLATFORM CHOICE:

Since we are using CPU-based approaches to parallelize different SAT solvers, the computer we use does not need GPU. Instead, we chose two different platforms with different vendors, number of cores, and ability of hyperthreading to study the capabilities of our parallelizing approaches and how much we can leverage from the resources provided.

As for the language, C/C++ is chosen due to our possible parallelizing approaches using OpenMP/OpenMPI. With previous experience in those tools, we believe the familiarity will enable us to focus on those problems.

## SCHEDULE:


    Week 1 (11/12-11/18): Develop a project proposal and set up a development environment. Perform preliminary literature review on the chosen SAT solvers and parallelizing branching algorithms. 


    Week 2 (11/19-11/25): Implement sequential implementations of the chosen SAT solver algorithms. Establish benchmarks for performance comparisons. Begin to implement parallel versions of chosen algorithms. 


    Week 3 (11/26-12/02): Implement parallel versions of chosen algorithms. 


    Week 4 (12/03-12/09): Finish implementing parallel versions of chosen algorithms. Begin scalability testing and performance analysis.


    Week 5 (12/09-12/15): Compile results to create final report and presentation poster. Present final project at project poster session. 

