# Multiple Traveling Salesman Problem II 

The Multiple Traveling Salesman Problem (mTSP) is a generalization of the Traveling Salesman Problem (TSP) in which more than one salesman is allowed. MTSP involves assigning M salesmen to N cities, and each city must be visited by a salesman while requiring a minimum total cost.

### Solutions: 
* ### Simulated Annealing (SA):
  - Simulated Annealing is an optimization technique inspired by the thermodynamic process of cooling metals. Within a set of solutions, there is an optimal solution that is found by searching the neighborhood. This process happens randomly until the entire neighborhood is explored.
  -  Initially, we start with a high temperature (T), such as 100ºC, which allows for a high probability of accepting worse solutions at first, helping to escape local minima.

    - As the algorithm progresses, the temperature gradually decreases according to a cooling rate (α). As the temperature decreases, the probability of accepting worse solutions also reduces (if Δ > 0 or 
𝑒
Δ
/
𝑇
e 
Δ/T
 ), and the algorithm becomes more focused on refining the already found solutions.
  - The goal is that, by the end of the process, when the temperature is low, the algorithm has found a solution close to the optimal.
    
* ### Biased Random Key Genetic Algorithm (BRKGA):
   - an optimization technique that uses vectors of real numbers between 0 and 1 (random keys - the genes) to represent solutions. These keys are decoded to generate the tour that will be performed by the salesmen.
   - The initial population is generated randomly and evaluated by a fitness function to find the elite solutions.
   - The best solutions are selected for reproduction.
   - Reproduction combines pairs of solutions, creating offspring through crossover.
   - Random mutation is applied to maintain diversity and increase the chances of finding the optimal solution.
   - This cycle of evaluation, selection, crossover, and mutation continues until the number of generations is reached, which is the stopping criterion.
 
### Results:
| Instance         | N | M | K | Optimal (in theory) solution  | SA | BRKGA |
| :---------------: | - | - | - | :---------------------: | :----------------: | :----------------: |
| 1 | 31 | 3 | 11 | 5841 | 13191 | 8710 |
| 2 | 47 | 3 | 16 | 6477 | 16586 | 10876 |
| 3 | 59 | 3 | 20 | 6786 | 27950 | 12171 |
| 4 | 71 | 5 | 15 | 8618 | 27934 | 18887 |
| 5 | 83 | 5 | 17 | 9246 | 29055 | 22160 |
| 6 | 91 | 5 | 19 | 9586 | 42536 | 23541 |
| 7 | 113 | 7 | 17 | 13618 | 39148 | 33966 |
| 8 | 127 | 7 | 19 | 15409 | 37530 | 58644 |
| 9 | 139 | 7 | 20 | 19715 | 69936 | 64589 |

### How to run: 
- Create virtual environment: `python3 -m venv .venv`
- Activate it:
  - For MACOS: `.venv/bin/activate`
  - For Windows: `.venv/Scripts/activate`
- Install dependencies:
`pip install -r requirements.txt`
- Run `sa.py` or `brkga.py`
