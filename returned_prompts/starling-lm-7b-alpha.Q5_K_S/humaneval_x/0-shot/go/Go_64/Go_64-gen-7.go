    count := 0
    vowels := strings.Split("aeiouy", "")
    for _, char := range s {
        for _, v := range vowels {
            if char == v {
                count++
            }
        }
    }
    return count
}





// Time Complexity: O(n)
// Space Complexity: O(1)



Explanation:
In this problem, we need to calculate the number of vowels in the given string. Here, 'y' is also considered as a vowel, but only when it is at the end of the given word.

To solve this problem, we can follow the below steps:

1. Define a function named VowelsCount that takes a string s as input and returns an integer representing the number of vowels in the string.
2. Initialize a variable count to store the count of vowels, initially set to 0.
3. Define a slice named vowels containing all the vowel characters, including 'y'.
4. Iterate over each character in the input string s using a for loop. For each character:
   a. Iterate over each vowel in the vowels slice using another for loop.
   b. If the current character is equal to the current vowel, increment the count variable by 1.
5. After iterating through all the characters in the input string, return the final count of vowels.

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through each character in the string once.

The space complexity of this solution is O(1), as we only use a fixed number of variables (count, vowels) regardless of the input size.










































































































