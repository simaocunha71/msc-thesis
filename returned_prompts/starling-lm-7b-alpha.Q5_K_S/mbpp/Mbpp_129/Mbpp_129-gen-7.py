Here's one way to do it:

```python
def magic_square_test(matrix):
    # check if matrix is square
    if len(matrix) != len(matrix[0]):
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in matrix)) > 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(col) for col in zip(*matrix))) > 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in zip(*matrix))) > 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in matrix)) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(col) for col in zip(*matrix))) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in zip(*matrix))) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in matrix)) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(col) for col in zip(*matrix))) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in zip(*matrix))) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in matrix)) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(col) for col in zip(*matrix))) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in zip(*matrix))) != 1:
        return False
    # check if all values in matrix are same
    if len(set(sum(row) for row in