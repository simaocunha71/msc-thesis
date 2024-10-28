    # Find the depth of each group
    # If the group is empty, return 0
    # If the group is not empty, return the maximum of the depth of the leftmost and rightmost parts of the group

    # Split the input into groups separated by spaces
    groups = paren_string.split(" ")

    # Initialize an empty list to store the maximum depth of each group
    depths = []

    # Iterate through each group
    for group in groups:
        # If the group is empty, return 0
        if not group:
            depths.append(0)
        # If the group is not empty, return the maximum of the depth of the leftmost and rightmost parts of the group
        else:
            # Split the group into leftmost and rightmost parts
            leftmost, rightmost = group.split("(", 1)
            # Get the depth of the leftmost and rightmost parts
            leftmost_depth = len(leftmost) - len(leftmost.lstrip("("))
            rightmost_depth = len(rightmost.rstrip(")")) - len(rightmost)
            # Get the maximum depth of the leftmost and rightmost parts
            max_depth = max(leftmost_depth, rightmost_depth)
            # Append the maximum depth to the list
            depths.append(max_depth)

    return depths
