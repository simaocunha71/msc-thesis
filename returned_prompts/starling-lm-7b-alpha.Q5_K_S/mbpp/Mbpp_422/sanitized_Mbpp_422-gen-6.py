def find_Average_Of_Cube(n):
    """
    Find the average of cubes of the first n natural numbers.
    """
    # Calculate the sum of cubes of the first n natural numbers
    sum_cubes = (n*(n+1)/2)**2
    # Divide the sum by n to find the average
    average = sum_cubes / n
    # Return the average
    return average