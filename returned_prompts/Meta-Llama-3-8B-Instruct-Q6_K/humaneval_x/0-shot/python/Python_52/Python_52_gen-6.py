    def below_threshold(l: list, t: int):
        for i in l:
            if i >= t:
                return False
        return True
    # Test cases
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
    # Explanation: This function iterates over the list and checks if any element is greater than or equal to the threshold. If it finds such an element, it immediately returns False. If it doesn't find any, it returns True after checking all elements. The time complexity is O(n), where n is the length of the list.