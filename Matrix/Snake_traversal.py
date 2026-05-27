def snake_traversal(matrix):

    if not matrix or not matrix[0]:
        return 
    
    row_len = len(matrix)
    col_len = len(matrix[0])

    for i in range(row_len):
        if i % 2 == 0:
            for j in range (col_len):
                print(matrix[i][j], end = " ")
        
        else:
            for j in range(col_len-1, -1, -1):
                print(matrix[i][j], end = " ")
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
snake_traversal(matrix)