


N = 4

def printSolution (sol):

    for i in sol:
        for j in i:
            print (str(j) + " ", end = " ")
        print("")


def IsGoodMove (maze, x, y):
    if x > 0 and x < N and y > N and y < N and maze[x][y] == 1:
        return True
    else:
        return False


def SolveMaze (maze):
    sol = [ [ 0 for j in range(10)] for i in range(10) ]

    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Løsning findes ikke")
        return False

    printSolution(sol)
    return True

def solveMazeUtil(maze, x, y, sol):
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    if IsGoodMove