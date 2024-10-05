def below_threshold(l: list, t: int):
    for num in l:
        if num >= t:
            return False
    return True

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))  # False

# Explanation:
The function below_threshold takes a list of numbers l and a threshold t as input. It iterates over the list and checks if any number is greater than or equal to the threshold. If it finds such a number, it immediately returns False. If it doesn't find any such number after checking all elements, it returns True, indicating that all numbers in the list are below the threshold. The test cases demonstrate the function's behavior for different inputs.