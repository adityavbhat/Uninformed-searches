Class DFS:
    def depthFirstSearch(start_state):
        stack = LifoQueue()
        stack.put((start_state, [], 0, 0))
        visited = set()
        generated_number = 0
        popped_number = 0
        maximumFringe = 1

        if dump_flag:
            with open('output.txt', 'a') as f:
                output_String = "\n Depth First Search\n"
                f.write(output_String)
        else:
            print("\n Depth First Search")
        while not stack.empty():
            state, path, cost, depth = stack.get()
            if dump_flag:
                with open('output.txt', 'a') as f:
                    output_String = "State {}\n".format(state)
                    f.write(output_String)
            else:
                print("\nDepth First Search\n")
            popped_number += 1
            if state == GOAL_STATE:
                return (path, cost, generated_number, num_popped, maximumFringe, depth)
            if (tuple(map(tuple, state))) in visited:
                continue
            visited.add(tuple(map(tuple, state)))
            for successor, step_cost in reversed(list(generate_successors(state))):
                generated_number += 1
                stack.put((successor, path + [(state, successor)], cost + step_cost, depth + 1))
                maximumFringe = max(maximumFringe, stack.qsize())
        return (None, None, generated_number, num_popped, maximumFringe, None, None)


