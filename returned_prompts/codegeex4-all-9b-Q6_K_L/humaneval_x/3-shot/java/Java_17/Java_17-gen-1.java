
hasCloseElements
Your code is correct, and it's pretty simple.
However, there are a few small improvements that could be made:

You could use a for-each loop instead of the traditional for loop, which makes the code a little bit more readable.
Instead of calling Math.abs() on the result of numbers.get(i) - numbers.get(j), you could use Math.abs(numbers.get(i) - numbers.get(j)), which is equivalent but shorter.
You could use a break statement instead of the return statement to exit the loop when a close element is found.

Here's the improved code:

public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (Double number : numbers) {
        for (Double otherNumber : numbers) {
            if (number.equals(otherNumber)) continue;
            if (Math.abs(number - otherNumber) < threshold) return true;
        }
    }
    return false;
}

separateParenGroups
Your code is correct, and it's pretty simple.
However, there are a few small improvements that could be made:

You could use a StringBuilder to build the current_string, which is more efficient than using the + operator.
You could use a while loop instead of the for loop, which makes the code a little bit more readable.
You could use a break statement instead of the return statement to exit the loop when a close element is found.

Here's the improved code:

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

truncateNumber
Your code is correct, and it's pretty simple.
However, there are