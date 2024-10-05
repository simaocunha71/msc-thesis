
Your code looks good, and it's not really easy to suggest improvements since the code is quite straight forward and does what it's supposed to do.
One thing that I would like to note is that you should be using Long instead of long for the return type of specialFactorial since it can go beyond the maximum value that long can hold.
Also, you can use the built-in Math library to calculate the factorial of a number instead of manually calculating it. This will reduce the complexity of your code. Here's how you can do it:
public long specialFactorial(int n) {
    long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
        result *= Math.factorial(i - 1);
    }
    return result;
}

Another thing is that you can use StringBuilder instead of String to build your strings in separateParenGroups method. This will be more efficient since StringBuilder is mutable and doesn't create a new object every time you append a character to it. Here's how you can do it:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();
    int current_depth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_depth += 1;
            current_string.append(c);
        } else if (c == ')') {
            current_depth -= 1;
            current_string.append(c);

            if (current_depth == 0) {
                result.add(current_string.toString());
                current_string.setLength(0);
            }
        }
    }
    return result;
}

Overall, your code is good and does what it's supposed to do. You can make it more efficient and readable by using StringBuilder instead of String and Math library to calculate the factorial of a number.