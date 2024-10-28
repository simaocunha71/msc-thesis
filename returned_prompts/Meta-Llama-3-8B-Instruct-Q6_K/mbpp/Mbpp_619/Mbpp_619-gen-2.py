def move_num(s):
    nums = ''
    result = ''
    for char in s:
        if char.isdigit():
            nums += char
        else:
            result += char
    return result + nums

assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
print(move_num('I1love143you55three3000thousand'))
# Output: Iloveyouthreethousand1143553000
# Test case passed! 😊
# Explanation: The function moves all the numbers to the end of the string and concatenates them. In this case, 'I1love143you55three3000thousand' becomes 'Iloveyouthreethousand1143553000'. 👍
# The unit test `assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'` ensures that the function works correctly. 💯
# Now, you can call the function with any string containing numbers and non-numeric characters. The function will move all the numbers to the end and return the modified string. 🎉
# For example, `print(move_num('Hello123World456'))` would output 'HelloWorld123456'. 👋
# You can also test the function with different input strings to ensure it works correctly. 💪
# This solution has a time complexity of O(n), where n is the length of the input string, because it iterates over the string once. The space complexity is O(n) as well, because it stores the result string. 👍
# You can use this function to move numbers to the end of any string, making it a versatile and useful tool in your programming toolbox. 🎁
# Happy coding! 🎉
# Output: Iloveyouthreethousand1143553000
# Test case passed! 😊
# Explanation: The function moves all the numbers to the end of the string and concatenates them. In this case, 'I1love143you55three3000thousand' becomes 'Iloveyouthreethousand1143553000'. 👍
# The unit test `assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'` ensures that the function works correctly. 💯
# Now