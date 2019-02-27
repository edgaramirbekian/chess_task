import chess

def input_coords ():
    black_king = input('Coordinates of the black King --- ')

    white_king = input('Coordinates of the white King --- ')
    white_queen = input('Coordinates of the white Queen --- ')
    white_bishop = input('Coordinates of the white Bishop --- ')
    white_knight = input('Coordinates of the white Knight --- ')
    all_white_moves = (chess.getKingMoves(white_king) + chess.getQueenMoves(white_queen) + chess.getBishopMoves(white_bishop) + chess.getKnightMoves(white_knight))
    all_white_moves.sort()

    all_white_moves_nodupl = []
    for item in all_white_moves:
        if item not in all_white_moves_nodupl:
            all_white_moves_nodupl.append(item)

    black_king_moves = chess.getKingMoves(black_king)
    # print(all_white_moves_nodupl)
    # print (chess.getKingMoves(black_king))

    flag = True
    for item in black_king_moves:
        if item in all_white_moves_nodupl:
            continue
        else:
            flag = False
            break

    if flag == True:
        print('Checkmate !!!')
    else:
        print ('No Checkmate :( Try Again')
        input_coords()

input_coords ()