import chess

def check_usr_input (user_input):
    if len(user_input) == 2 and user_input[0] >= 'a' and user_input[0] <= 'h' and int(user_input[1]) >= 1 and int(user_input[1]) <= 8:
        pass
    else:
        inp = input ('You have entered uncorrect coordinates. Try Again y/n ')
        if inp.lower() == 'y':
            input_coords()
        else:
            print('bye')

def input_coords ():

    black_king = input('Coordinates of the black King --- ')
    check_usr_input(black_king)
    white_king = input('Coordinates of the white King --- ')
    check_usr_input(white_king)
    white_queen = input('Coordinates of the white Queen --- ')
    check_usr_input(white_queen)
    white_bishop = input('Coordinates of the white Bishop --- ')
    check_usr_input(white_bishop)
    white_knight = input('Coordinates of the white Knight --- ')
    check_usr_input(white_knight)

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
        again = input ('No Checkmate :( Try Again ? y/n ')
        if again.lower() == 'y':
            input_coords()
        else:
            print('bye')

input_coords ()