        // Check if text contains whitespace
        if (txt.contains(" ")) {
            return Arrays.asList(txt.split(" "));
        }

        // Check if text contains comma
        else if (txt.contains(",")) {
            return Arrays.asList(txt.split(","));
        }

        // Count lowercase letters with odd order in the alphabet
        else {
            int count = 0;
            for (char c : txt.toCharArray()) {
                if (Character.isLowerCase(c) && (c - 'a') % 2 != 0) {
                    count++;
                }
            }
            return count;
        }
    }
}

Here is the code, the function `splitWords` takes a string `txt` as input and returns a list of words split by either spaces, commas, or returns the number of lower-case letters with odd order in the alphabet.

If the string contains a space, the function splits the string at each space and returns the result as a list.

If the string contains a comma, the function splits the string at each comma and returns the result as a list.

If the string does not contain a space or a comma, the function counts the number of lower-case letters with odd order in the alphabet and returns this count.

Here are some test cases:

```java
System.out.println(new Solution().splitWords("Hello world!")) // ["Hello", "world!"]
System.out.println(new Solution().splitWords("Hello,world!")) // ["Hello", "world!"]
System.out.println(new Solution().splitWords("abcdef")) // 3
```

The function works by using the `split` method of the `String` class to split the string at each occurrence of a specified character. The `Character.isLowerCase` method is used to check if each character is a lower-case letter, and the `(c - 'a') % 2 != 0` expression checks if the order of the letter in the alphabet is odd.

The `Arrays.asList` method is used to convert the resulting array of strings into a list.

The `System.