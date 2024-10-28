        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (Character.isLowerCase(c)) {
                sb.append(Character.toUpperCase(c));
            } else {
                sb.append(Character.toLowerCase(c));
            }
        }
        return sb.toString();
    }
}
class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.flipCase("Hello"));
    }
}
```

This Java program defines a method `flipCase` that takes a string as input and returns a new string where all lowercase characters are converted to uppercase and all uppercase characters are converted to lowercase. The `Main` class provides a test case to demonstrate the functionality of the `flipCase` method.

Here's a breakdown of how the code works:

1. The `flipCase` method takes a string as input and initializes an empty `StringBuilder` object `sb`.
2. The method iterates over each character `c` in the input string using a `for` loop.
3. For each character, it checks if the character is lowercase using the `Character.isLowerCase` method. If it is, the method converts the character to uppercase using the `Character.toUpperCase` method and appends it to the `StringBuilder` object `sb`.
4. If the character is not lowercase, it is assumed to be uppercase, and the method converts it to lowercase using the `Character.toLowerCase` method and appends it to the `StringBuilder` object `sb`.
5. The method returns the resulting string by calling the `toString` method on the `StringBuilder` object `sb`.

In the `Main` class, an instance of the `Solution` class is created, and the `flipCase` method is called with the input string "Hello". The resulting string is then printed to the console. The output is "hELLO", which demonstrates the correct functionality of the `flipCase` method.