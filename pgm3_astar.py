def aStarAlgo(start, stop):
    open_set, closed_set, g, parents = {start}, set(), {start: 0}, {start: start}

    while open_set:
        n = min(open_set, key=lambda x: g[x] + heuristic(x))

        if n == stop or not Graph_nodes.get(n):
            pass
        else:
            for m, weight in get_neighbors(n) or []:
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                elif g[m] > g[n] + weight:
                    g[m], parents[m] = g[n] + weight, n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        if not n:
            print('Path does not exist!')
            return None

        if n == stop:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print('Path found:', path)
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n, 0)

Graph_nodes = {'A': [('B', 2), ('E', 3)], 'B': [('C', 1), ('G', 9)], 'C': None, 'E': [('D', 6)], 'D': [('G', 1)]}
aStarAlgo('A', 'G')
