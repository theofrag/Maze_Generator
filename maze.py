import random
from PIL import Image


class Cell:
    def __init__(self,x,y):
        self.visited=False
        self.walls={'Down':True,'Right':True}
        #Coordinates of the cell
        self.x=x
        self.y=y
    
    #changes the state of a wall
    def changeState(self,direction):
        self.walls[direction]=False
    #get the state of a wall
    def getState(self,direction):
        return self.walls[direction]
    def getValues(self):
        return list(self.walls.values())

class Grid:
    def __init__(self,rows,cols):
        self.grid= [[Cell(i,j) for j in range(cols)]for i in range(rows)]
        self.stack=[]
        #dimensions of the grid
        self.row=rows
        self.col=cols
        #current position
        self.x=0
        self.y=0
    
    def getNeighbors(self,x,y):
        list=[]
        if(x+1<self.row and (self.grid[x+1][y].visited==False)):
            list.append(self.grid[x+1][y])
        if(x-1>=0 and (self.grid[x-1][y].visited==False)):
            list.append(self.grid[x-1][y])
        if(y+1<self.col and (self.grid[x][y+1].visited==False)):
            list.append(self.grid[x][y+1])
        if(y-1>=0 and (self.grid[x][y-1].visited==False)):
            list.append(self.grid[x][y-1])
        return list
    

    def makeMaze(self):
        
        #insert 1st cell into stack
        self.stack.insert(0,self.grid[self.x][self.y])

        #initialize 1st cell as visited
        self.grid[self.x][self.y].visited=True

        #while stack is not empty
        while self.stack:
            
                
            #take the list of neighbors
            list= self.getNeighbors(self.x,self.y)
            
            #if list is not empty
            if list:
                #choose an arbitary neighbor
                random_num=random.choice(list)
                
                i=random_num.x
                j=random_num.y
                
                #break walls
                if self.x-i<0 and self.y-j==0:
                    self.grid[self.x][self.y].changeState('Down')
                elif self.x-i>0 and self.y-j==0:
                    self.grid[i][j].changeState('Down')
                elif self.x-i==0 and self.y-j<0:
                    self.grid[self.x][self.y].changeState('Right')
                elif self.x-i==0 and self.y-j>0:
                    self.grid[i][j].changeState('Right')
                #update current position
                self.x=i
                self.y=j
                #cell is visited
                self.grid[self.x][self.y].visited=True
                #insert the new cell into the stack
                self.stack.insert(0,self.grid[self.x][self.y])
            elif not list :
                popped_element=self.stack.pop(0)
                self.x=popped_element.x
                self.y=popped_element.y
                
    
    def outputMaze(self):
        
        img=Image.new('RGB',(self.col*2,self.row*2),(0,0,0))
        for i in range(self.row):
            for j in range(self.col):
                img.putpixel((2*j,2*i), (255,255,255))
                if self.grid[i][j].getState('Right')==False:
                    img.putpixel((2*j+1,2*i),(255,255,255))
                if self.grid[i][j].getState('Down')==False:
                    img.putpixel((2*j,2*i+1),(255,255,255))

        img.save('maze.png')


grid=Grid(5,5)
grid.makeMaze()
grid.outputMaze()


