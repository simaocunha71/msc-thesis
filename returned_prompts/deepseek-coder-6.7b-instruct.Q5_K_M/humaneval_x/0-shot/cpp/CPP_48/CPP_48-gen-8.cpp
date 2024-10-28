    int start = 0;
    int end = text.length() - 1;

B:
    while (start < end){
        if (text[start] != text[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main() {
    printf(is_palindrome("") ? "true" : "false");
    printf(is_palindrome("aba") ? "true" : "false");
    printf(is_palindrome("aaaaa") ? "true" : "false");
    printf(is_palindrome("zbcd") ? "true" : "false");
    return 0;
}
```

You can compile this program and run it, and you should get the expected output for all the test cases.

**Explanation:**

This program uses a while loop to check the characters at the start and end of the string. If the characters are not the same, it returns false. If the characters are the same, it increments the start index and decrements the end index to check the next pair of characters. This process continues until the start index is no longer less than the end index. If all pairs of characters were the same, the function returns true.

The main function tests the `is_palindrome` function with four different test cases and prints the result.

**Time complexity:**

The time complexity of this program is O(n), where n is the length of the string. This is because the program needs to iterate over half of the string to check if it's a palindrome.

**Space complexity:**

The space complexity of this program is O(1), because it only uses a fixed amount of space to store the start and end indices of the string, regardless of the size of the string.

This is a simple solution, but it demonstrates the basic idea of how to solve the problem.

**Note:** This program assumes that the input is always a string. If the input could be a number or a different type, you would need to add additional error checking to ensure that the input is a string.

**Note:** This program is case sensitive, meaning it considers 'a' and 'A' as different