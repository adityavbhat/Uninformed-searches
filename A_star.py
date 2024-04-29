Class A_Star:
    def a_star(start_state):
        queue = PriorityQueue()
        queue.put((heuristic(start_state), start_state, [], 0, 0))
        visited = set()
        generated_number = 0
        popped_number = 0
        maximumFringe = 1

        if dump_flag:
            with open('output.txt','a') as f:
                output_String = "\n A Star Search \n"
                f.write(output_String)
        else:
            print("\n A Star Search \n")
        while not queue.empty():
            _, state, path, cost, depth = queue.get()
            if dump_flag:
                with open('output.txt','a') as f:
                    output_String = "State for A Star: {}\n".format(state)
                    f.write(output_String)
            else:
                print("State of A Star: {}".format(state))
            popped_number += 1
            if state == GOAL_STATE:
                return (path, cost, generated_number, num_popped, maximumFringe, depth)
            if tuple(map(tuple, state)) in visited:
                continue
            visited.add(tuple(map(tuple, state)))
            for successor, step_cost in generate_successors(state):
                generated_number += 1
                queue.put(heuristic(successor) + cost + step_cost, successor, path +[(state, successor)], cost + step_cost, depth + 1)
                maximumFringe = max(maximumFringe, queue.qsize())
        return (None, None, generated_number, num_popped, maximumFringe, None, None)

