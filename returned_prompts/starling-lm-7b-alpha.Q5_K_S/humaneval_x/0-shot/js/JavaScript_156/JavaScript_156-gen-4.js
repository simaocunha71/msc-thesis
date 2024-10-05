
Explanation:
The function `intToMiniRoman` takes a single argument, a positive integer `number`. It initializes an empty string `roman` to store the resulting Roman numeral and a variable `i` to keep track of the current denomination being checked.

The function uses an object `numeralMappings` to map each Roman numeral value to its corresponding integer value. The object is sorted in descending order, starting with the largest denomination, 1000, and ending with the smallest denomination, 1.

The function enters a while loop, which continues until the `number` becomes 0. Inside the loop, it finds the largest denomination that is less than or equal to the current `number` using the `find` method on the keys of `numeralMappings`. It then appends the corresponding Roman numeral to the `roman` string and subtracts the integer value from the `number`. After that, it updates the `i` variable by dividing it by 10 to move to the next denomination.

Once the `number` becomes 0, the loop exits, and the function returns the `roman` string, which represents the Roman numeral equivalent of the input `number`.

The provided test cases demonstrate that the function correctly converts the input integer to its Roman numeral representation in lowercase