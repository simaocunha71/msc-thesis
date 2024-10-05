from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (None, None)
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the pair of closest numbers
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the pair of closest numbers
    return closest_pair
    # end of find_closest_elements
# end of find_closest_elements
# end of Q
# end of A
# end of file
# end of file
# end of file
# end of file

# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
# end of file
#