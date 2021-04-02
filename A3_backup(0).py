import utils
class Solution(object):
    def leastNumBus(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        print(routes)
        busTaken = [False for _ in range (len(routes))]     #inti with all bus not Taken
        current = source    #indicate current station
        stationTravel = [source]    #inti with communter only its start point
        possibleNextStation = []    #for retrieve (BFS)
        counter = 0

        for busIdx in range (len(routes)):
            if routes[busIdx].count(current) == 1:
                removeCurrent = routes[busIdx]
                removeCurrent.remove(current)
                possibleNextStation.append({busIdx:removeCurrent})      #ref: https://stackoverflow.com/questions/15738700/a-quick-way-to-return-list-without-a-specific-element-in-python
        print(possibleNextStation)

        while (len(possibleNextStation)):   #program run until there are no possible next step
            for bus in possibleNextStation:
                for stations in bus.values():    #bus is dict with idx i
                    
                    for station in stations:     #stations is list of stations of that bus with idx i
                        print(station)

            break

        print(possibleNextStation)


        if current == source:
            return -1
            






if __name__ == '__main__':
    utils.score()

