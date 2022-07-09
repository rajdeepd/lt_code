from typing import List

from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        l = []
        if len(edges) == 0 and source == 0 and destination == 0:
            return True
        count = 0
        for e in edges:
            start = e[0]
            end = e[1]

            if len(l) == 0:
                if start == source and count == 0:
                    l.append(start)
                    l.append(end)
            else:

                l_end = l[len(l)-1]
            # print(l_end)
                if start == l_end:
                    l.append(end)
            if len(l) > 0 and l[len(l) - 1] == destination:
                return True
            print(l)
            ++count

        print(l)
        if len(l) > 0 and l[len(l) - 1] == destination:
            return True
        else:
            return False

    def validPathTwo(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = dict();

        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False] * n
        dq = deque([source])

        while dq:
            node = dq.popleft()

            for nbr in graph[node]:
                if nbr == destination:
                    return True
                elif not visited[nbr]:
                    visited[nbr] = True
                    dq.append(nbr)
        return False
sol =  Solution()
# n1 = 6
# edges1 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# start1 = 0
# destination1 = 5
# result1 = sol.validPath(n1,edges1,start1,destination1)
# print(result1 == True)
# n2 = 3
# edges2 = [[0,1],[1,2],[2,0]]
# start2 = 0
# destination2 = 2
# result2 = sol.validPath(n2,edges2,start2,destination2)
# print('result2 == True:',result2 == True)

# n3 = 1
# edges3 =[]
# s3 =0
# d3 =0
# expected3 = True
#
# result3 = sol.validPath(n3,edges3,s3,d3)
# print('result3 == ' + str(expected3) + ' : ' + str(result3 == True))

n4 = 10
edges4 =[[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
s4 = 5
d4 = 9
expected4 = True

result4 = sol.validPathTwo(n4,edges4,s4,d4)
print('result4 == ' + str(expected4) + ":" + str(result4 == expected4))




