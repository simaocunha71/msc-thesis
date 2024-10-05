        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <= n; i++) {
            sb.append(i).append(" ");
        }
        return sb.toString().trim();
    }
}

Explanation:

1.  We use a `StringBuilder` object to efficiently build the string sequence.
2.  We iterate from 0 to `n` (inclusive) using a `for` loop.
3.  Inside the loop, we append the current number `i` to the `StringBuilder` object followed by a space using the `append` method.
4.  After the loop, we use the `toString` method to convert the `StringBuilder` object to a string.
5.  Finally, we use the `trim` method to remove the trailing space from the resulting string.

Output:
For `n = 5`, the output will be `"0 1 2 3 4 5"`. For `n = 0`, the output will be `"0"`.