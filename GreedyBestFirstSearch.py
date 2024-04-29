Class GBFS:
    def greedyBestFirstSearch(start_state):
        queue = PriorityQueue()
        queue.put((euclidean_distance(start_state), start_state, [], 0, 0))
        visited = set()
        generated_number = 0
        popped_number = 0
        maximumFringe = 1

        if dump_flag:
            with open('output.txt','a') as f:
                output_String = "\n Greedy Search \n"
                f.write(output_String)
        else:
            print("\n Greedy Search \n")
        while not queue.empty():
            _, state, path, cost, depth = queue.get()
            if dump_flag:
                with open('output.txt', 'a') as f:
                    output_String = "State: {}\n".format(state)
                    f.write(output_String)
            else:
                print("State of Greedy Search: {}\n".format(state))

            popped_number += 1
            if state == GOAL_STATE:
                return (path, cost, generated_number, num_popped, maximumFringe, depth)
            if tuple(map(tuple, state)) in visited:
                continue
            visited.add(tuple(map(tuple, state)))
            for successor, step_cost in generate_successors(state):
                generated_number += 1
                priority = euclidean_distance(successor)
                queue.put((priority, successor, path + [(state, successor)], cost +step_cost, depth + 1))
                maximumFringe = max(maximumFringe, queue.qsize())
        return (None, None, generated_number, num_popped, maximumFringe, None, None)

    def euclidean_distance(state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0
                    target_i, target_j = divmod(state[i][j] - 1, 3)
                    distance += ((i - target_i) ** 2 + (j - target_j) **2) ** 0.5
        return distance
