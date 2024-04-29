2232-CSE-5360-001
Artificial Intelligence I


Name: Aditya Vikram Bhat
UTA ID: 1002014494


Programming language used: Python 3.10.7


- Each search strategy is defined in a separate file each and is called by the main function.

- The user is required to input the start and the goal state respectively along with the value of dump flag in the command prompt to execute the program.

- Each search strategy is defined in their respective files as classes and inherited by the main function for performing the required searches.

- We find the coordinates of the tiles and the numbers stored in each tiles in the start state using the get_tile_coords function.

- I have used euclidean distance between two points as the heuristic function for greedy and A* search strategies.

- For moves, I have used a tuple with 4 values of up, down, left, right, respectively, which specifies the movement that the empty tile/ the tile adjacent to it will move to/from.

- The given program removes the redundant moves that one will face when it traverses in a node.

- The use of various data structures has been utilised for the implementation of these search strategies.

- Namely: queue for Breadth First Search, stack for Depth First Search, priority queue for Uniform Cost Search, euclidean distance heuristic for greedy and A* search and iterative (recursive) function call of dfs for Iterative Deepening Search and Depth Limited Search.

- Install python modules using the command pip install python in command prompt or use an IDE such as Pycharm or online service like Google Colab to run the code.

- Open command prompt and enter the following commands: cd Directory of file where it is located (downloads for example)

- Use the respective names for using the search that you want to perform.

- For Breadth First Search, enter the following line of command in terminal: python expense_8_puzzle.py start.txt goal.txt breadthFirstSearch

- For Depth First Search, enter the following line of command in terminal: python expense_8_puzzle.py start.txt goal.txt depthFirstSearch
  
- For Uniform Cost Search, enter the following line of command in terminal: python expense_8_puzzle.py start.txt goal.txt uniformCostSearch

- For A Star Search, enter the following line of command in terminal: python expense_8_puzzle.py start.txt goal.txt a_star

- For Greedy Best First Search, enter the following line of command in terminal: python expense_8_puzzle.py start.txt goal.txt greedyBestFirstSearch

- For Iterative Deepening Search, enter the following line of command in terminal: python expense_8_puzzle.py start.txt goal.txt iterativeDeepeningSearch

- For Depth Limited Search, enter the following line of command in terminal: python expense_8_puzzle.py start.txt goal.txt depthLimitedSearch

- To generate the iterations in an output file, put dump_flag as true after the name of the search strategy in the command line.

