# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

hard1 =[[0,8,0,0,0,2,0,0,0],
        [9,0,5,0,0,0,0,4,0],
        [0,0,0,3,1,0,0,6,0],
        [0,3,0,0,0,0,0,8,0],
        [5,0,0,0,6,0,0,3,0],
        [7,0,4,0,0,5,0,0,9],
        [0,0,0,0,4,0,9,0,0],
        [0,0,0,0,0,7,0,0,0],
        [0,0,6,1,0,0,4,0,0]]

def check_sudoku(grid):
    ###Your code here.
    
    ###Check the lengths
    if len(grid) != 9:
        return None
    for i in range(0,9):
        if len(grid[i])!=9:
            return None
    
    
    ### Check rows
    i = 0
    j = 0
    for i in range(0,9):
        for j in range(0,8):
            k = j+1
            if grid[i][j]==0:
                continue
            for k in range(j+1,9):
                if grid[i][k]==0:
                    continue
                if grid[i][j]==grid[i][k]:
                    return False
                k+=1
            j+=1
        i+=1
                

    ###Check columns
    i = 0
    j = 0
    for i in range(0,9):
        for j in range(0,8):
            k = j+1
            if grid[j][i]:
                continue
            for k in range(j+1,9):
                if grid[k][i]==0:
                    continue
                if grid[j][i]==grid[k][i]:
                    return False
                k+=1
            j+=1
        i+=1
        
    ###Check squares
    myList = [0,3,6,9]
    i = 0
    j = 0
    k = 0
    l = 0
    for i in range(myList[k],myList[k+1]):
        for k in range(myList[l],myList[l+1]):
            mySquare=[]
            if grid[i][k] not in mySquare:
                mySquare.append(grid[i][k])
            else:
                return False
            k+=1
        i+=1

    return True
    pass

def print_grid(grid):
    if grid == None:
        print(None)
        return False
    
    elif not grid:
        print(False)
        return False
    
    for row in grid:
        print(row)
        
    print("\n")
    


def getZeroesList(grid):
    
    Zeroes= []
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j]==0:
                Zeroes.append([i,j])

    return Zeroes
    pass

def DeepCopy(grid):
    if grid==None:
        return None
    myGrid = []
    for i in range(0,9):
        myGrid.append(grid[i])
    return myGrid        

def solveSudoku(grid,Zeroes,i):
    
    SolutionList = GetSolutionList(grid,Zeroes,i)
    myGrid=DeepCopy(grid)
    
    for j in range(0,len(SolutionList)):
        myGrid[Zeroes[i][0]][Zeroes[i][1]]=SolutionList[j]
        tempGrid = DeepCopy(myGrid)
        if check_sudoku(myGrid):
            if i!= len(Zeroes)-1:
                temp2Grid = solveSudoku(myGrid,Zeroes,i+1)
                if temp2Grid == None:
                    ###Replace 0s in the unsolved cells
                    j+=1
                    myGrid = DeepCopy(tempGrid)
                    for k in range(i+1,len(Zeroes)):
                        myGrid[Zeroes[k][0]][Zeroes[k][1]]=0
                    continue
                else:
                    return temp2Grid
            else:
                return myGrid
            
        else:
            j+=1
    
    return None
        
pass

def GetSolutionList(grid,Zeroes,i):
    j = Zeroes[i][0]
    SolutionList=[1,2,3,4,5,6,7,8,9]
    for k in range(0,9):
        if grid[j][k] in SolutionList:
            SolutionList.remove(grid[j][k])
        k+=1
    
    j = Zeroes[i][1]
    for k in range(0,9):
        if grid[k][j] in SolutionList:
            SolutionList.remove(grid[k][j])
        k+=1
    
    SquareBounds =[0,3,6,9]
           
    sq_lbx=SquareBounds[int((Zeroes[i][0])/3)]
    sq_lby=SquareBounds[int((Zeroes[i][1])/3)]
    sq_ubx=SquareBounds[int((Zeroes[i][0])/3)+1]
    sq_uby=SquareBounds[int((Zeroes[i][1])/3)+1]
        
    for j in range(sq_lbx,sq_ubx):
        for k in range(sq_lby, sq_uby):
            if grid[j][k] in SolutionList:
                SolutionList.remove(grid[j][k])
            k+=1
        j+=1
    
    return SolutionList
pass
    
def solve_sudoku (grid):
    
    ###Your code here.
    
    i = 0
    j = 0
    
    is_valid = check_sudoku(grid)
    if not is_valid or is_valid == None:
        return is_valid
    
    
    ###Check for 0s in the grid and find the possible values of numbers
    
    Zeroes=getZeroesList(grid)
    ###Get Solution List for each of the 'Zeroes'
    if(len(Zeroes)==0):
        return grid
    
    Numbers = [1,2,3,4,5,6,7,8,9]
    SolutionList =[]
   
    ###Find possible values for the Zeroes 
    myGrid = solveSudoku(grid,Zeroes,0)
    
    return myGrid
pass

myGrid = solve_sudoku(ill_formed)
print_grid(myGrid)

myGrid = solve_sudoku(valid)
print_grid(myGrid)

myGrid = solve_sudoku(easy)
print_grid(myGrid)

myGrid = solve_sudoku(invalid)
print_grid(myGrid)
    
myGrid = solve_sudoku(hard)
print_grid(myGrid)

myGrid = solve_sudoku(hard1)
print_grid(myGrid)




