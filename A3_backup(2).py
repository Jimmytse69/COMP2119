import utils
class Solution(object):
    def leastNumBus(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        
        #convert routes to adj_list and nodes

        nodes = []
        for bus in routes:
            for node in bus:
                nodes.append(node)
        Nodes = sorted(list(set(nodes)))    #remove duplicate Nodes and sort it
        adj_list = [[] for _ in range(len(Nodes))]  #create # of nodes of [] for adjacency list

        for node_idx in range(len(Nodes)):  #assign sorted order of nodes name to 0,1,2,...,len(nodes)-1
            for bus in routes:
                if Nodes[node_idx] in bus:  
                    for station in bus:
                        if station != Nodes[node_idx]:  #if that node exist in that bus route, and there are other nodes, append it to adj_list because that node can reach there.
                            adj_list[node_idx].append(station)


        Adj_list = []
        for l in adj_list:
            l = sorted(list(set(l)))    #remove duplicate and sort it
            Adj_list.append(l)

        #Now, Nodes is like dictionary key, coorispond to Adj_list contain its' "reachable" infomation
        
        #print(Nodes)
        #print(Adj_list)

        #Apply dijkstra Algo next to find shortest path.
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
                for edge_to_not_yet_translate in g[minIndex]:
                    edge_to = Nodes.index(edge_to_not_yet_translate)
                    if vis[edge_to]:     #check the edge_to is visted
                        continue
                    else:
                        new_dist = dist[minIndex] + 1   #1 is the cost
                    if new_dist < dist[edge_to]:
                        prev[edge_to] = minIndex
                        dist[edge_to] = new_dist
                        pq.append((edge_to, new_dist))
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
        
        #call it to find shortest path
        
        path = find_shortest_path(Adj_list, len(Nodes), Nodes.index(source), Nodes.index(target))    #need to translate back to "Adj_list" cooridinate system, i.e. 0,1,...n-1
        
        Path = []
        #translate back to "Nodes value" cooridinates
        for node in path:
            Path.append(Nodes[node])
        


        #write a "Back-tracking" recusive algo to retrive shortest route, DFS
        bus_counter = 0
        if Path == []:
            bus_counter = -1
        
        
                




        
            
        return bus_counter



        








if __name__ == '__main__':
    utils.score()

