Class BFS:
    def breadthFirstSearch(start_state):
        queue = Queue()
        queue.put((start_state, [], 0, 0))
        visited = set()
        generated_number = 0
        popped_number = 0
        maximumFringe = 1

        if dump_flag:
            with open('output.txt', 'a') as f:
                output_String = "\nBreadth First Search\n"
                f.write(output_String)
        else:
            print("\nBreadth First Search\n")
        while not queue.empty():
            state, cost, path, depth = queue.get()
            if dump_flag:
                with open('output.txt', 'a') as f:
                    output_String = "State: {}\n".format(state)
                    f.write(output_String)
            else:
                print("State of Breadth first search: {}\n".format(state))
            popped_number += 1
            if state == GOAL_STATE:
                return (path, cost, generated_number, num_popped, maximumFringe, depth)
            if tuple(map(tuple, state)) in visited:
                continue
            visited.add(tuple(map(tuple, state)))
            for successor, step_cost in generate_successors(state):
                generated_number += 1
                queue.put((successor, path + [(state, successor)], cost + step_cost, depth + 1))
                maximumFringe = max(maximumFringe, queue.qsize())
        return (None, None, generated_number, num_popped, maximumFringe, None, None)
