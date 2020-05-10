"""chessDictionaryValidator"""

testBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "8e": "wking",
    "3f": "wking"
}


def isValidChessBoard(board):

    # Check if white and black king are around

    if "bking" not in board.values() or "wking" not in board.values():
        print("One side has no king...")
        return False

    # Check if the amount of figures and their placements on the field are ok

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

    l_locations = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for location, figure in board.items():

        if location[-1] in l_locations and int(location[0]) in range(1, 9):
            pass
        else:
            print("Location not on the board")
            return False

        if figure == "wking":
            wking += 1
            if wking > validation.get(figure):
                return False
        elif figure == "bking":
            bking += 1
            if bking > validation.get(figure):
                return False
        elif figure == "wpawn":
            wpawn += 1
            if wpawn > validation.get(figure):
                return False
        elif figure == "bpawn":
            bpawn += 1
            if bpawn > validation.get(figure):
                return False
        elif figure == "wqueen":
            wqueen += 1
            if wqueen > validation.get(figure):
                return False
        elif figure == "bqueen":
            bqueen += 1
            if bqueen > validation.get(figure):
                return False
        elif figure == "wknight":
            wknight += 1
            if wknight > validation.get(figure):
                return False
        elif figure == "bknight":
            bknight += 1
            if bknight > validation.get(figure):
                return False
        elif figure == "wbishop":
            wbishop += 1
            if wbishop > validation.get(figure):
                return False
        elif figure == "bbishop":
            bbishop += 1
            if bbishop > validation.get(figure):
                return False
        elif figure == "wrook":
            wrook += 1
            if wrook > validation.get(figure):
                return False
        elif figure == "brook":
            brook += 1
            if brook > validation.get(figure):
                return False

    if wking < 1 or wking > 1 or bking < 1 or bking > 1 or wqueen > 1 or bqueen > 1 or wbishop > 2 or bbishop > 2 or wrook > 2 or brook > 2 or wknight > 2 or bknight > 2 or wpawn > 8 or bpawn > 8:
        return False
    else:
        return True


print(isValidChessBoard(testBoard))
