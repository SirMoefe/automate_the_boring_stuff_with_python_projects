"""chessDictionaryValidator"""

testBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking"
}


def isValidChessBoard(board):

    # Check if white and black king are around

    if "bking" not in board.values() or "wking" not in board.values():
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

        if location[-1] in l_locations and location[0] in range(1, 8):
            pass
        else:
            print("Location not on the board")
            return False

        if figure == "wking":
            wking += 1
        elif figure == "bking":
            bking += 1
        elif figure == "wpawn":
            wpawn += 1
        elif figure == "bpawn":
            bpawn += 1
        elif figure == "wqueen":
            wqueen += 1
        elif figure == "bqueen":
            bqueen += 1
        elif figure == "wknight":
            wknight += 1
        elif figure == "bknight":
            bknight += 1
        elif figure == "wbishop":
            wbishop += 1
        elif figure == "bbishop":
            bbishop += 1
        elif figure == "wrook":
            wrook += 1
        elif figure == "brook":
            brook += 1

    if wking < 1 or wking > 1 or bking < 1 or bking > 1 or wqueen > 1 or bqueen > 1 or wbishop > 2 or bbishop > 2 or wrook > 2 or brook > 2 or wknight > 2 or bknight > 2 or wpawn > 8 or bpawn > 8:
        return False


"""figureCount_white = wking + wqueen + wknight + wbishop + wrook + wpawn
    figureCount_black = bking + bqueen + bknight + bbishop + brook + bpawn
    if figureCount_white > 16 or figureCount_black > 16:
        return False """
