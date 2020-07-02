tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    #Create Table to figure out the longest string in each table
    columWidth = [0] * len(table)
    for y in range(len(table)):
        for x in table[y]:
            if len(x) > columWidth[y]:
                columWidth[y] = len(x)
    print(columWidth)


printTable(tableData)