
Solution 1:
Your code looks good and it's well organized. You can add a few comments to make it even better.

Solution 2:
Your code is correct and efficient. However, you can make it more readable by using a while loop instead of a for loop.
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

Solution 3:
Your code is correct and efficient. However, you can make it more readable by using a while loop instead of a for loop.
public double truncateNumber(double number) {
    return number % 1.0;
}

Solution 4:
Your code is correct and efficient. However, you can make it more readable by using a while loop instead of a for loop.
public List<Integer> factorize(int n) {
    List<Integer> result = new ArrayList<>();
    int current_prime = 2;

    while (n > 1) {
        if (n % current_prime == 0) {
            result.add(current_prime);
            n /= current_prime;
        } else {
            current_prime += 1;
        }
    }
    return result;
}