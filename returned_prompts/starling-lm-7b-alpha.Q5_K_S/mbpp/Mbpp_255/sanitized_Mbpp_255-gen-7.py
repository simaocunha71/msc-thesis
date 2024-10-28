def combinations_colors(colors,n):
    '''
    Args:
        colors(list): List of colors
        n(int): length of each combination
    Returns:
        list: List of tuples containing all combinations
    '''
    # Initialize result
    result = []
    for i in range(len(colors)):
        # Check if length is 1
        if n == 1:
            result.append((colors[i],))
        else:
            # Generate all combinations
            result.extend(combinations_colors(colors[:i]+colors[i+1:],n-1))
    return result