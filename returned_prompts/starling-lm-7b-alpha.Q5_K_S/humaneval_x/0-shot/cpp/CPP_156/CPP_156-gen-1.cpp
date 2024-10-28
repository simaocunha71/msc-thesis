To solve this problem, we can use a recursive function to generate all the Roman numeral strings and compare them to the target number until we find a match. Here's a step-by-step explanation of how to do it:

1. Define a vector of Roman numeral strings, from "i" to "m". This will be used to generate all possible Roman numeral representations of integers.
2. Create a recursive function called `int_to_mini_romank` that takes an integer as input and returns a string representing its Roman numeral equivalent. The function works as follows:
   - If the input number is less than the length of the `numbers` vector, return the corresponding Roman numeral string at that index.
   - If the input number is greater than or equal to the length of the `numbers` vector, subtract the current number from the input number, and recursively call `int_to_mini_romank` with the