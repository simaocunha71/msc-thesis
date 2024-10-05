        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <= n; i++) {
            sb.append(i).append(" ");
        }
        return sb.toString().trim();
    }
}

Solution solution = new Solution();
System.out.println(solution.stringSequence(5)); // prints "0 1 2 3 4 5"

Explanation:
1. We use a StringBuilder to efficiently build the string.
2. We iterate from 0 to n (inclusive) using a for loop.
3. Inside the loop, we append the current number to the StringBuilder followed by a space.
4. After the loop, we call `toString()` on the StringBuilder to get the resulting string.
5. We use `trim()` to remove the trailing space at the end of the string.
6. The final result is a space-delimited string of numbers from 0 to n.