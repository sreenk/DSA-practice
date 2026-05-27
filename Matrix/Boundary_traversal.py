def boundary_traversal(matrix):
    if not matrix or not matrix[0]:
        return
    
    row_len = len(matrix)
    col_len = len(matrix[0])
    
    for j in range(col_len):
        print(matrix[0][j], end = " ")
    
    for i in range(1, row_len):
        print(matrix[i][col_len-1], end = " ")
    
    for j in range(col_len-2,-1,-1):
        print(matrix[row_len-1][j], end = " ")
    
    for i in range(row_len-2, 0,-1):
        print(matrix[i][0], end = " ")
    
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
boundary_traversal(matrix)