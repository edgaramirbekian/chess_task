chessBoard = [['x'] * 8 for i in range(8)]
map_from_alpha_to_index = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}
map_from_index_to_alpha = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}

def checkAppend (x,y, solutions_arr):
    if x >= 0 and y >= 0:
        solutions_arr.append([x,y])

def parseChessCoords (machine_coords):
    possibleMoves = ["".join([map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in machine_coords]
    possibleMoves.sort()
    return possibleMoves

def getKnightMoves(pos, board = chessBoard):
    
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []

    try:
        checkAppend(i+1, j-2, solutionMoves)
    except:
        pass

    try:
        checkAppend(i+2, j-1, solutionMoves)
    except:
        pass

    try:
        checkAppend(i+2, j+1, solutionMoves)
    except:
        pass

    try:
        checkAppend(i+1, j+2, solutionMoves)
    except:
        pass

    try:
        checkAppend(i-1, j+2, solutionMoves)
    except:
        pass

    try:
        checkAppend(i-2, j+1, solutionMoves)
    except:
        pass

    try:
        checkAppend(i-2, j-1, solutionMoves)
    except:
        pass

    try:
        checkAppend(i-1, j-2, solutionMoves)
    except:
        pass
    
    all_moves = parseChessCoords(solutionMoves)
    print(all_moves)
    return all_moves

getKnightMoves('d4')

def getBishopMoves (pos, board = chessBoard):

    

