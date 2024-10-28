
Solution 1

Your solution has a time complexity of O(n^2). This is because you are using nested for loops to iterate through the list. You can improve this by using a single for loop and keeping track of the minimum and maximum values.

Here is an improved version of the code:

public boolean hasCloseElements(List<Double> numbers, double threshold) {
    double min = Double.MAX_VALUE;
    double max = Double.MIN_VALUE;

    for (double number : numbers) {
        if (number < min) {
            min = number;
        }
        if (number > max) {
            max = number;
        }
    }

    return (max - min) < threshold;
}

Solution 2

Your solution has a time complexity of O(n^2). This is because you are using nested for loops to iterate through the list. You can improve this by using a single for loop and keeping track of the minimum and maximum values.

Here is an improved version of the code:

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

Solution 3

Your solution has a time complexity of O(n). This is because you are using a single for loop to iterate through the list. However, you are not checking if the number is between 1 and 9 inclusive.

Here is an improved version of the code:

public double truncateNumber(double number) {
    return number % 1.0;
}

Solution 4

Your solution has a time complexity of O(n^2). This is because