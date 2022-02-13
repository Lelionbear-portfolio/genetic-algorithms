# Genetic Algorithms

#### Frameworks
> Numerous Python frameworks have been created for working with genetic algorithms—GAFT, Pyevolve, and PyGMO, to mention a few. After looking into several options, we chose to use the DEAP framework for this book, thanks to its ease of use and a large selection of features, as well as its extensibility and ample documentation.

### One Max Problem
##### File(s): [OneMaxProblem01], [OneMaxProblem02], [OneMaxProblem03]
The One Max Problem is an introductory approach to the DEAP framework as you attempt to fill in an array with all 1's. 
Each file is progressively condense as the utilization of DEAP is explored and explained.
#### Population Size and number of generations
Some analysis of `POPULATION_SIZE` is that it affects the performace of the program, if larger the faster the solution is achieved thru younger generations while if smaller the longer the solution is achieved with distant generations (it could potentially not converge as well - no solution). If no convergence is achieved then the number of `MAX_GENERATIONS` can be incremented to attempt a smaller population size but with more possible generations.

#### Crossover
Using a Single-point crossover (`tools.cxOnePoint`) we reach convergence at the 40th generation while a Two-point crossover (`tools.cxTwoPoint`) would reach convergence at the 27th generation.

#### Mutation
The variable `P_MUTATION` determines the probability that an individual from the population would get selected for a mutation. While the mutation-related parameter in the algorithm, `indpb=`, which is an argument of the specific mutation operator we used here `tools.mutFlipBit` determines the propability of how much of the individual's "genes" get mutated. This can be either beneficial or not as an excess probability of mutations would lead to a random search for convergence and not make any progress towards it. 

#### Tournament size and relation to mutation probability
When the `tournsize=` parameter of `tools.selTournament` is increased and the `P_MUTATION` is adequate:
> the chance of weak individuals being selected diminishes, and better solutions tend to take over the population. In real-life problems, this takeover might cause suboptimal solutions to saturate the population and prevent the best solution from being found (a phenomenon known as **premature convergence**)

When the `P_MUTATION` is below adequate but the `tournsize=` is increased:
> the best individuals from the initial population take over within a small number of generations....
> 
> After that, only an occasional mutation in the right direction—one that flips a 0 to 1—creates a better individual....
> 
> Soon after, this individual <ins>takes over</ins> the entire population again....

Whenever a "takeover" occurs due to the population becoming saturated by "best individuals" a higher `P_MUTATION` allows for more competiton between individuals to reach a convergence.

<!-- #### Roulette Wheel Selection and Elitist Approach 
**TODO** -->


[OneMaxProblem01]: OneMaxProblem01.py
[OneMaxProblem02]: OneMaxProblem02.py
[OneMaxProblem03]: OneMaxProblem03.py