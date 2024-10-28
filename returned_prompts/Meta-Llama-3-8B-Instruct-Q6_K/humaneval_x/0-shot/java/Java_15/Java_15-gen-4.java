        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <= n; i++) {
            sb.append(i).append(" ");
        }
        return sb.toString().trim();
    }
}
Solution solution = new Solution();
String result = solution.stringSequence(5);
System.out.println(result); // prints "0 1 2 3 4 5"





Output: 0 1 2 3 4 5
Explanation: The given code creates a new StringBuilder object and appends each number from 0 to n (inclusive) to it. A space is appended after each number. Finally, the toString() method is called on the StringBuilder object to get the resulting string, and the trim() method is used to remove the trailing space.

Complexity Analysis:
Time complexity: O(n), where n is the input number. This is because the code iterates over the range from 0 to n.
Space complexity: O(n), where n is the input number. This is because the code uses a StringBuilder object to store the resulting string, and the size of the string is proportional to the input number.