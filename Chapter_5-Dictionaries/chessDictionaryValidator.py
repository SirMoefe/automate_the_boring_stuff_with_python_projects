"""chessDictionaryValidator"""

testBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "8e": "wking",
    "9f": "wbishop"
}


def isValidChessBoard(board):

    # Check if white and black king are around

    if "bking" not in board.values() or "wking" not in board.values():
        print("One side has no king...")
        return False

    # Check if the amount of pieces and their placements on the field are ok

    validation = {"wking": 1, "bking": 1, "wqueen": 1, "bqueen": 1, "wbishop": 2,
                  "bbishop": 2, "wrook": 2, "brook": 2, "wknight": 2, "bknight": 2, "wpawn": 8, "bpawn": 8}
    wking = 0
    bking = 0
    wqueen = 0
    bqueen = 0
    wbishop = 0
    bbishop = 0
    wrook = 0
    brook = 0
    wknight = 0
    bknight = 0
    wpawn = 0
    bpawn = 0

    letter_locations = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for location, piece in board.items():

        if location[-1] in letter_locations and int(location[0]) in range(1, 9):
            pass
        else:
            print("Location not on the board")
            return False
        if piece not in validation:
            print("Unknown piece on the field")
            return False
        else:
            if piece == "wking":
                wking += 1
                if wking > validation.get(piece):
                    print("Too many white kings on the board")
                    return False
            elif piece == "bking":
                bking += 1
                if bking > validation.get(piece):
                    print("Too many white kings on the board")
                    return False
            elif piece == "wpawn":
                wpawn += 1
                if wpawn > validation.get(piece):
                    print("Too many white kings on the board")
                    return False
            elif piece == "bpawn":
                bpawn += 1
                if bpawn > validation.get(piece):
                    print("Too many white kings on the board")
                    return False
            elif piece == "wqueen":
                wqueen += 1
                if wqueen > validation.get(piece):
                    print("Too many white queens on the board")
                    return False
            elif piece == "bqueen":
                bqueen += 1
                if bqueen > validation.get(piece):
                    print("Too many black queens on the board")
                    return False
            elif piece == "wknight":
                wknight += 1
                if wknight > validation.get(piece):
                    print("Too many white knights on the board")
                    return False
            elif piece == "bknight":
                bknight += 1
                if bknight > validation.get(piece):
                    print("Too many black knights on the board")
                    return False
            elif piece == "wbishop":
                wbishop += 1
                if wbishop > validation.get(piece):
                    print("Too many white bishops on the board")
                    return False
            elif piece == "bbishop":
                bbishop += 1
                if bbishop > validation.get(piece):
                    print("Too many black bishops on the board")
                    return False
            elif piece == "wrook":
                wrook += 1
                if wrook > validation.get(piece):
                    print("Too many white brooks on the board")
                    return False
            elif piece == "brook":
                brook += 1
                if brook > validation.get(piece):
                    print("Too many black brooks on the board")
                    return False
    return True


print(isValidChessBoard(testBoard))
