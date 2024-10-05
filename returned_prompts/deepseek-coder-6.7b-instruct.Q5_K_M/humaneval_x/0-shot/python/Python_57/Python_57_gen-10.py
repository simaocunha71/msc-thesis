
    if len(l) < 2:
        return True

    if l[0] < l[1]:
        for i in range(2, len(l)):
            if l[i-1] > l[i]:
                return False
    else:
        for i in range(2, len(l)):
            if l[i-1] < l[i]:
                return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# The function first checks if the list has less than two elements. If so, it returns True as there is no need for comparison. 
# Then it checks if the first element is less than the second. 
# If true, it checks if the next elements in the list are greater than the previous ones. 
# If any of them are not, the function returns False. 
# If the first element is not less than the second, it means the list is monotonically decreasing. The function then checks if the next elements are less than the previous ones. 
# If any of them are not, the function returns False. 
# If no discrepancy is found after all elements are checked, the function returns True. 
# Finally, the doctest module is used to test the function with the provided examples.

# The function uses a loop to check each pair of adjacent elements in the list. If it finds a pair where the next element is not greater or not less than the previous one, it immediately returns False. If it doesn't find such a pair after checking all elements, it returns True.

# The time complexity of this function is O(n), where n is the length of the list. This is because it checks each element in the list once. The space complexity is O(1), as it uses a constant amount of space to store the indices and the list elements.
<jupyter_output>
<empty_output>
<jupyter_text>
