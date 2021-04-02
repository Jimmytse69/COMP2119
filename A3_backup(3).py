import utils
class Solution(object):
    def leastNumBus(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        num_of_route = len(routes)  #how many buses routes it have
        source_bus_list = []    #what buses can commutor from source take
        target_bus_list = []    #what buses can directly reach to end point overall

        for route_idx in range(num_of_route):
            if source in routes[route_idx]:
                source_bus_list.append(route_idx)
            if target in routes[route_idx]:
                target_bus_list.append(route_idx)
        
        #find all combination of source_bus_route to target_bus_route
        combs_of_start_to_target = []
        for source_bus in source_bus_list:
            for target_bus in target_bus_list:
                combs_of_start_to_target.append((source_bus, target_bus))

        #generate a graph of Adj_list represent routes connectivity (not station!)\
        #done by compare distince bus_route have same station or not.

        Adj_list = []
        counter = 0
        for route_idx1 in range(num_of_route):
            route_idx1_connection_list = []
            for route_idx2 in range (num_of_route):
                if route_idx1 != route_idx2:
                    #https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists
                    if len(list(set(routes[route_idx1]).intersection(routes[route_idx2]))) != 0:
                        route_idx1_connection_list.append(route_idx2)
            Adj_list.append(route_idx1_connection_list)
            counter += 1


        #from each (source_bus, target_bus) pair in combs_of_sta...
        #use shorest path(route) Algo find min one.

        #function disjkstra and find_shortest_path is directly reference from
        #https://www.youtube.com/watch?v=pSqmAO-m7Lk&t=773s 
        def dijkstra(g, n, s):
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
                    if vis[edge_to]:     #check the edge_to is visted
                        continue
                    else:
                        new_dist = dist[minIndex] + 1   #cost = 1
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

        #end of Shortest Path Algo

        #find min in those shortest paths

        no_path = False
        Paths = []
        for pair in combs_of_start_to_target:
            p = find_shortest_path(Adj_list, len(Adj_list), pair[0], pair[1])
            Paths.append(p)
        
        len_of_paths = []
        for path in Paths:
            len_of_paths.append(len(path))
            if path == []:
                no_path = True

        result = min(len_of_paths)

        if no_path == True:
            result = -1
        if source == target:
            result = 0

        return result
        


            
    

if __name__ == '__main__':
    utils.score()

