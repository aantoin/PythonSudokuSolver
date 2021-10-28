def solve(board):
    rows = [set(y for y in board[x*9:(x+1)*9] if y!=0) for x in range(9)]
    cols = [set(y for y in board[x:81:9] if y!=0) for x in range(9)]
    grids= [[set(z for i,z in enumerate(board) if (i%9)//3==x and i//(9*3)==y and z!=0) for x in range(3)] for y in range(3)]
    def solveSpace(i):
        if i == 81:
            return True
        if board[i]!=0:
            return solveSpace(i+1)
        row = rows[i//9]
        col = cols[i%9]
        grid = grids[i//9//3][i%9//3]
        available = set(i+1 for i in range(9))-row-col-grid
        if(len(available)==0):
            return False
        for v in available:
            row.add(v)
            col.add(v)
            grid.add(v)
            if solveSpace(i+1):
                board[i]=v
                return True
            else:
                row.remove(v)
                col.remove(v)
                grid.remove(v)
        return False
    return solveSpace(0)


f = open("sudoku_tests.txt","r")
for line in f:
    line = line.rstrip()
    puzzle, result, solution = (line.split(":")+[None])[:3]
    puzzle  = [int(v) if v!='.' else 0 for v in puzzle]

    solved = solve(puzzle)
    puzzle = "".join(str(v) for v in puzzle)

    if int(solved) == int(result):
        if solved:
            if puzzle != solution:
                print(len(puzzle))
                print(len(solution))
                print(f"Incorrect Solution\n{line}")
                input()
            else:
                print(f"Correct {line}")
        else:
                print(f"Correct {line}")
    else:
        print(f"Failed to solve\n{line}")
