    arr = list(map(str, arr))  # Convert all elements to strings
    arr = arr + arr[::-1][1:]  # Add the reverse of the array (excluding the first element) to the end
    arr = list(set(arr))  # Remove duplicates
    return len(arr) - 1  # Return the number of elements minus one (since we added one more element)  # Return the number of elements minus one (since we added one more element)  # Return the number of elements minus one (since we added one more element)


