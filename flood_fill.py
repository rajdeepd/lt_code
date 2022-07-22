from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #print(image)
        #print('sr', sr)
        #print('sc', sc)
        rows = len(image)
        columns = len(image[0])

        val = image[sr][sc]
        print(image[sr-1][sc])
        print(image[sr+1][sc])
        #print(image[sr - 1][sc], image[sr][sc - 1])
        #print(image[sr-1][sc] == val and image[sr][sc-1] == val)
        image[sr][sc] = color
        #for i in range (0, len(image))
        if sr-1 >=0 and sc-1 >=0 and image[sr-1][sc] == val and image[sr][sc-1] == val:
            image[sr - 1][sc-1] = color
        #print(image[sr][sc-1])
        print(image[sr + 1][sc] == val)
        print(sr + 1 <= rows - 1 and sc - 1 >= 0 and image[sr + 1][sc] == val and image[sr][sc + 1] == val and image[sr][sc-1] == val)
        if sr + 1 <= rows - 1 and sc - 1 >= 0 and image[sr + 1][sc] == val and image[sr][sc + 1] == val and image[sr][sc-1] == val:
            image[sr + 1][sc - 1] = color
        #print('image[sr - 1][sc]',image[sr - 1][sc])
        #print('image[sr+1][sc + 1]', image[sr+1][sc + 1])
        #print('sr + 1 <= rows - 1 and sc + 1 <= columns-1 and image[sr - 1][sc] == val and image[sr+1][sc + 1] == val',
        #      sr + 1 <= rows - 1 and sc + 1 <= columns-1 and image[sr - 1][sc] == val and image[sr+1][sc + 1] == val)
        if sr + 1 <= rows - 1 and sc + 1 <= columns-1 and  sc-1>0 and image[sr - 1][sc] == val and image[sr+1][sc + 1] == val:
            print(sr+1, sc-1)
            image[sr + 1][sc - 1] = color
        #print(image[sr][sc-1] == val and image[sr+1][sc] == val)

        if  sr-1 >=0 and image[sr - 1][sc] == val:
            image[sr - 1][sc] = color
            #print(image[sr - 1][sc + 1])
            if image[sr - 1][sc + 1] == val:
                image[sr - 1][sc + 1] = color
            if image[sr - 1][sc - 1] == val:
                image[sr - 1][sc - 1] = color
        if sr+1 <= rows-1 and image[sr + 1][sc] == val:
            image[sr + 1][sc] = color
            if image[sr + 1][sc + 1] == val:
                image[sr + 1][sc + 1] = color
            if image[sr + 1][sc - 1] == val:
                image[sr + 1][sc - 1] = color
        if  sc-1 >=0 and image[sr][sc - 1] == val:
            image[sr][sc - 1] = color
        i = 1
        while i <= columns-1:
            #print(i)
            if sc + i <= columns -1 and image[sr][sc + i] == val:
                image[sr][sc + i] = color
            i = i + 1
        if sr - 1 >= 0 and image[sr-1][sc] == val:
            image[sr - 1][sc] = color

        return image

sol = Solution()
# image1 = [[1,1,1],[1,1,0],[1,0,1]]
# sr1 =1
# sc1 =1
# color1 = 2
# response1 = str(sol.floodFill(image1,sr1,sc1,color1))
# expected1 = '[[2,2,2],[2,2,0],[2,0,1]]'
# print('response1:', response1)
# print('expected1:', expected1)
# print('response1 == expected1', response1 == expected1)
#
# print('-'*50)
# image2 = [[0,0,0],[0,0,0]]
# sr2 =1
# sc2 =0
# color2 = 2
# response2 = sol.floodFill(image2,sr2,sc2,color2)
# print('response2:', response2)

# image3 =[[0,0,0],[0,0,1]]
# sr3 = 0
# sc3 = 0
# color3 = 2
# response3 = sol.floodFill(image3,sr3,sc3,color3)
# expected3 = '[[2, 2, 2], [2, 2, 1]]'
# print('response3:', response3)
# print('expected3:', expected3)
# print('response3 == expected3', response3 == expected3)


image4 = [[1,1,1],[1,1,0],[1,0,1]]
sr4 =1
sc4 =1
color4 =2
response4 = sol.floodFill(image4,sr4,sc4,color4)
expected4 = '[[2, 2, 2], [2, 2, 0], [2, 0, 1]]'
print('response4:', response4)
print('expected4:', expected4)
print('response4 == expected4', response4 == expected4)
