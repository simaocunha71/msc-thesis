
Your solutions look good, but here are some suggestions:

In the first solution, you can use a for-each loop instead of the for loops:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size() - 1; i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

In the second solution, you can use a StringBuilder to build the current string and then convert it to a String when adding it to the result list:
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

In the third solution, you can use the Math.floor function to truncate the number:
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

In the fourth solution, you can use a for loop to iterate over the numbers in the list and add them to the collatz list if they are odd:
public List<Integer> getOddCollatz(int n) {
    List<Integer> collatz = new ArrayList<>();
    for (int i = n; i > 1; i = collatzStep(i)) {
        if (i % 2 != 0) collatz.add(i);
    }
    return collatz;
}