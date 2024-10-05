The code provided is correct and it will give the expected output. It first converts the given integer N to a binary string using `strconv.FormatInt` function. Then it iterates over each character in the binary string. If the character is '1', it increments the sum. Finally, it converts the sum to a string and returns it.

Here is the step-by-step execution of the code:

1. For N = 1000:
   - `strconv.FormatInt(int64(N), 2)` returns the binary representation of 1000, which is "11001000".
   - The loop iterates over each character in the binary string. The sum is initialized to 0.
   - The first character is '1', so the sum is incremented to 1.
   - The rest of the characters are '0', so the sum remains 1.
   - The function returns the string "1".

2. For N = 150:
   - `strconv.FormatInt(int64(N), 2)` returns the binary representation of 150, which is "10010110".
   - The loop iterates over each character in the binary string. The sum is initialized to 0.
   - The first character is '1', so the sum is incremented to 1.
   - The next character is '0', so the sum remains 1.
   - The next character is '1', so the sum is incremented to 2.
   - The rest of the characters are '0',