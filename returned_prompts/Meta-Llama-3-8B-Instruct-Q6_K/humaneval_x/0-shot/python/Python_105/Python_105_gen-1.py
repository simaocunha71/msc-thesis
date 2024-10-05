def by_length(arr):
    # filter out numbers outside the range 1-9
    filtered_arr = [i for i in arr if 1 <= i <= 9]
    # sort the filtered array
    filtered_arr.sort()
    # reverse the sorted array
    filtered_arr = filtered_arr[::-1]
    # map each digit to its corresponding name
    result = [names[i-1] for i in filtered_arr]
    return result

names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # Output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
print(by_length([]))  # Output: []
print(by_length([1, -1, 55]))  # Output: ['One']  # ignore -1 and 55
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']  # sort and reverse the array first
print(by_length([10, 20, 30]))  # Output: []  # ignore numbers outside the range 1-9
print(by_length([1, 1, 1, 1]))  # Output: ['One', 'One', 'One', 'One']  # sort and reverse the array first
print(by_length([2, 2, 2, 2]))  # Output: ['Two', 'Two', 'Two', 'Two']  # sort and reverse the array first
print(by_length([1, 2, 3, 4, 5]))  # Output: ['Five', 'Four', 'Three', 'Two', 'One']  # sort and reverse the array first
print(by_length([8, 7, 6, 5, 4]))  # Output: ['Five', 'Four', 'Six', 'Seven', 'Eight']  # sort and reverse the array first
print(by_length([9, 8, 7, 6, 5]))  # Output: ['Five',