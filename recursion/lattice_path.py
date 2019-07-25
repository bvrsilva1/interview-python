

def calculate_lattice_path(rows, cols):

    """
    table = [[0] * cols for i in range(rows)]
    #rows
    print(len(table))
    #cols
    print(len(table[0]))
    """

    if rows == 0 and cols == 0:
        return 0
    else:
        return compute(rows, cols, 0, 0)


def compute(rows, cols, row, col):
    if row == rows and col == cols:
        return 1
    elif row > rows or col > cols:
        return 0
    else:
        down = compute(rows, cols, row + 1, col)
        right = compute(rows, cols, row, col + 1)
        return down + right


"""
#creating matrix
v = []
for i in range(n):
    v.append([0]* m)
"""

rows = 2
cols = 3

print(calculate_lattice_path(rows, cols))