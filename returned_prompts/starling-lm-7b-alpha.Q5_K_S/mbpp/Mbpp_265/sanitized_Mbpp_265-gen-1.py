def list_split(list_in, n):
    # Create an empty list to store the sublists
    sublists = [list_in[i:i + n] for i in range(0, len(list_in), n)]
    # Return the sublists
    return sublists