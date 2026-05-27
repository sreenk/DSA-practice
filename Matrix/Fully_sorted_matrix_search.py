def sorted_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return
    
    row_len = len(matrix)
    col_len = len(matrix[0])
    
    start = 0 
    end = (row_len * col_len)- 1
    
    while start <= end:
        mid = start + (end- start) // 2
        
        row = mid // col_len
        col = mid % col_len
        
        if matrix[row][col] == target:
            return (row,col)
        elif matrix[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1
    return (-1, -1)

matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15]
]
target = 9

print(sorted_matrix(matrix, target))
