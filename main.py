
import random, time, sys

maze = []
moves = [[1,0], [0,1], [-1,0], [0,-1]]
everyCell = []

start = [0,1]
class cell:
    def __init__(self, x, y, it):
        self.it = it
        self.x = x
        self.y = y
        self.state = "X"   # X = Wall, / = Path
        
    def checkWalls(self,maze):
        self.walls = []
        for c in moves:
            wallX = self.x+c[0]
            wallY = self.y+c[1]
            if wallX > -1 and wallX < sizeOfArray and wallY > -1 and wallY < sizeOfArray:
                adjWalls = 0
                wall = maze[wallX][wallY]
                if wall.state == "X":
                    self.walls.append(wall)
        return self.walls

    def checkAdj(self,maze):
        flag = False
        while flag == False:
            openPaths = 0
            self.myMove = random.choice(self.walls)
            for c in moves:
                adjX = self.myMove.x+c[0]
                adjY = self.myMove.y+c[1]
                if adjX > -1 and adjX < sizeOfArray and adjY> -1 and adjY < sizeOfArray:
                    if maze[adjX][adjY].state == "/":
                        openPaths += 1
                        if self.myMove in self.walls:
                            self.walls.remove(self.myMove)            
            if len(self.walls) == 0:
                return False
            if openPaths < 2:
                self.myMove.state="/"
                return self.myMove
            
def makeStack(maze):
    stack = []
    for c in maze:
        for r in c:
            if r.state == "/":
                stack.append(r)
    return stack

def gen(start,maze):
    loop = True
    currentCell = maze[1][1]
    iterations = int(sizeOfArray * (sizeOfArray/2))
    visited=0
    while loop:
        visited+=1
        if visited >= iterations:
            loop = False
        stack = []
        for c in maze:
            for r in c:
                if r.state=="/":
                    stack.append(r)
        longStack = len(stack)
        if len(stack) > 0:
            for value in stack:
                cellWalls = value.checkWalls(maze)
                c = value.checkAdj(maze)##cellWalls)
            if c != False:
                stack.remove(value)
                lastValue = c
    return maze, lastValue


def genMaze(sizeOfArray,start):
    maze =[]
    everyCell =[]
    iteration = 0
    for columns in range(int(sizeOfArray)):
        mazeRow = []
        for rows in range(int(sizeOfArray)):
            iteration += 1
            mazeRow.append(cell(columns,rows,iteration))
            everyCell.append(cell(columns,rows,iteration))
        maze.append(mazeRow)
    for c in maze:
        for r in c:
            if r.x == start[0] and r.y == start[0]:
                r.state = "/"
                firstValue = r
    maze, lastValue = gen(start,maze)
    return maze, lastValue, firstValue
            


make = []
moves = [[1,0], [0,1], [-1,0], [0,-1]]
everyCell = []
start = [0,1]
if len(sys.argv) > 1:
    try:
        sizeOfArray = int(sys.argv[1])
    except Exception as e:
        print(e)
else:
    sizeOfArray = input(">>>")
    sizeOfArray = int(sizeOfArray)
maze, lastValue, firstValue = genMaze(sizeOfArray,start)

print("-"*((sizeOfArray*2)+2))
for c in maze:
    for r in c:
        if r == lastValue:
            r.state="E"
        elif r == firstValue:
            r.state="S"
        print(r.state,end=' ')
    print()
print("-"*((sizeOfArray*2)+2))


                
            
