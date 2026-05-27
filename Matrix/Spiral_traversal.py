def spiral_traversal(matrix):
    if not matrix or not matrix[0]:
        return
    
    row_len = len(matrix)
    col_len = len(matrix[0])
    
    top = 0
    bottom = row_len - 1
    left = 0 
    right = col_len -1
    
    while top <= bottom and left <= right:
        for j in range(left,right+1):
            print(matrix[top][j], end = " ")
        top += 1
        
        for i in range(top, bottom+1):
            print(matrix[i][right], end = " ")
        
        right -= 1
        
        for j in range(right, left-1, -1):
            print (matrix[bottom][j], end = " ")
        
        bottom -= 1
        
        for i in range(bottom, top-1, -1):
            print (matrix[i][left], end = " ")
        
        left += 1
        
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
spiral_traversal(matrix)