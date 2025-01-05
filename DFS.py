import matplotlib.pyplot as plt
from collections import namedtuple
from utils import *
from npuzzle import NPuzzleState

Node = namedtuple('Node', 'state parent action cost')


def DFS(start_state, goal_state):
    explored = set()
    frontier = Stack()  # Use a stack instead of a queue for DFS
    frontier.push(Node(start_state, None, None, 0))
    Num_generated = 0

    while not frontier.is_empty():
        node = frontier.pop()
        if node.state in explored:
            continue  # Skip already visited nodes

        explored.add(node.state)

        if node.state == goal_state:
            return solution(node), Num_generated

        for successor, action, step_cost in node.state.successors():
            Num_generated += 1
            if successor not in explored:
                frontier.push(Node(successor, node, action, node.cost + step_cost))

    return None, Num_generated


# Test the DFS algorithm
start_state_tiles = [2, 8, 3, 6, 4, 7, 1, 0, 5]
goal_state_tiles = [1, 2, 3, 4, 0, 5, 6, 7, 8]
start_state = NPuzzleState(tiles=start_state_tiles)
goal_state = NPuzzleState(tiles=goal_state_tiles)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
start_state.plot(axes[0], "Start")
goal_state.plot(axes[1], "Goal")
plt.show()

solution_path, N = DFS(start_state, goal_state)
print(f"Number of generated nodes: {N}")
show_solution(start_state, solution_path, ncols=6)
