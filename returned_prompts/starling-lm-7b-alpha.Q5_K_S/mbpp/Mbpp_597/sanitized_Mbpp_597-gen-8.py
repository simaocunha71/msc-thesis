def find_kth(A, B, k):
    """
    Find the kth smallest element in two sorted arrays.

    Args:
        A (list): The first sorted array.
        B (list): The second sorted array.
        k (int): The position of the element to find.

    Returns:
        int: The kth smallest element from the two sorted arrays.
    """
    if k > len(A) + len(B):
        return None

    while len(A) > 0 and len(B) > 0 and k > 0:
        if A[0] < B[0]:
            k -= 1
            A.pop(0)
        else:
            k -= 1
            B.pop(0)

    if len(A) == 0:
        return B[0]
    elif len(B) == 0:
        return A[0]
    else:
        return None