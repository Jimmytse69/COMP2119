def dijkstra(g, n, s):
    #init
    vis = [False for _ in range(n)]
    prev = [None for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    pq = []     #empty priority queue
    pq.append((s, 0))
    while len(pq) != 0:
        minIndex = dist.index(min(dist))
        minValue = dist[minIndex]
        (minIndex, minValue) = pq.pop(0)
        vis[minIndex] = True
        for edge_to in g[minIndex]:
            if vis[edge_to[0]]:     #check the edge_to is visted
                continue
            else:
                new_dist = dist[minIndex] + edge_to[1]
            if new_dist < dist[edge_to[0]]:
                prev[edge_to[0]] = minIndex
                dist[edge_to[0]] = new_dist
                pq.append((edge_to[0], new_dist))
    return (dist, prev)

def find_shortest_path(g, n, s, e):
    dist, prev = dijkstra(g, n, s)
    path = []
    if (dist[e] == float("inf")): return path
    else:
        via = e
        while via != None:
            path.append(via)
            via = prev[via]
        path.reverse()
        return path

#g = adjacency list
g=[[[1,1],[2,5]],[[2,2],[4,6]],[[3,3]],[[4,2]],[]] # g[minIndex][i][0] = nodes, g[minIndex][i][1] = cost to from [i] to [i][0]
n = 5
s = 0
e = 4

#input testcase end!

print(dijkstra(g, n, s))
print(find_shortest_path(g, n, s, e))








        





