"""chessDictionaryValidator"""

testBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking"
}

validBoard = ["1a", "1b"]


def isValidChessBoard(board):
    if "bking" not in board or "wking" not in board:
        return False
    wking = 0
    bking = 0
    for figure in testBoard.values():
        if figure == "wking":
            wking += 1
        if figure == "bking":
            bking += 1
