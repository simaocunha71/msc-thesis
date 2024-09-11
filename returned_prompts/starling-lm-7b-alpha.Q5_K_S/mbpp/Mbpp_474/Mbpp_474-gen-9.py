def get_multiplication_matrix(A,B):
    if len(A[0])!=len(B):
        raise Exception("Can't multiply")
    C=[[0,0],[0,0]]
    for i