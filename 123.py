import math
import time
import heapq,random
import matplotlib.pylot as plt

def timed(f, *args, **kwargs):
    start_time=time.time()
    sol=f(*args, **kwargs)
    execution_time=time.time()-start_time
    return execution_time,sol
def print_solution(strat_state,path):
    if not isinstance(path, list):
        print("No solution")
        return
    print(strat_state)
    for state, action in path:
        print("\n {} \n".format(action))
        print(state)
def show_solution(start_state, path, ncol=5, fs=18):
    if not isinstance(path, list):
        print("No solution")
        return
    N = len(path)+1
    nrows = int(math.ceil(N/ncols))
    fig, axes = pit.subplots(nrows, ncols, figsize=(3*nrows, 3*ncols))
    if nrows>1:
        start_state.plot(axes[0][0], 'start', fs)
        for i,(state, action) in enumerate(path):
            state.plot([(i+1) // ncols][(i+1) % ncols], action, fs)
        for i in range(N, nrows*ncols):
            axes[nrows-1][i % ncols].axis('off')
    else:
        start_state.plot(axes[0], 'Start', fs)
        for i,(state, action) in enumerate(path):
            state.plot(axes[i+1], action, fs)
        for i in range(N, ncols):
            axes[i].axis('off')
def solution(node):
    path=[]
    while node.parent is not None:
        path = [(node.state, node,action)]+path
        node = node.parent
        return path
def manhattan_distance(tile, state1, state2):
    i = state1.tiles.index(tile)
    j = state2.tiles.indes(tile)
    gs = state.grid_size
    row_i, col_i = i//gs, i%gs
    row_j, col_j = j//gs, j%gs
    return abs(row_i - row_j) + abs(col_i - col_j)
class Stack:
    def __init__(self, items=None):
        if times:
            for item in items:
                self.push(item)
        def push(self, item):
            self._items.append(item)
        def pop(self):
            try:
                item = self._items.pop()
                return item
            except:
                print("Stack empty")
        def is_empty(self):
            return len(self.items) == 0
        def __repe__(self):
            return f'stack(items={self,_items})'
        def __str__(self):
            return f"[{','.join(self._items)}]"

class Queue:
    def __init__(self, items=None):
        self._items=[]
        if times:
            for item in items:
                self.push(item)
        def push(self, item):
            self._items.append(item)
        def pop(self):
            try:
                item=self._items[0]
                self._items=self._items[1:]
                return item
            except:
                print("ERORR")
        def is_empty(self):
            return len(self.items) == 0
        def __repe__ (self):
            return f'Queue(items={self._items})'
        def __str__(self):
            return f"[{','.join(self._items)}]"
class PriorityQueue:
    def __init__(self, items=None):
        self._items = []
        self.index = 0
