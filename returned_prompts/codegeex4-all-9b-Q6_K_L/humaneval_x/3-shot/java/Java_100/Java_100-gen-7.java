
Solution 1
The first problem is a simple search for two numbers which are closer to each other than a given threshold. The algorithm can be optimized by sorting the array first and then only checking the difference between the current number and the next one.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Collections.sort(numbers);
    for (int i = 0; i < numbers.size() - 1; i++) {
        double distance = Math.abs(numbers.get(i) - numbers.get(i + 1));
        if (distance < threshold) return true;
    }
    return false;
}

Solution 2
The second problem is to separate groups of parentheses in a string. This can be done by using a stack. The stack will store the open parentheses and when a closing parenthesis is encountered, the corresponding opening parenthesis will be removed from the stack. If the stack is empty at the end of the string, then all parentheses are balanced.
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();
    Stack<Character> stack = new Stack<>();

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            stack.push(c);
            current_string.append(c);
        } else if (c == ')') {
            current_string.append(c);
            stack.pop();

            if (stack.isEmpty()) {
                result.add(current_string.toString());
                current_string.setLength(0);
            }
        }
    }
    return result;
}

Solution 3
The third problem is to truncate a number to the decimal part. This can be done by subtracting the integer part from the number.
public double truncateNumber(double number) {
    return number - (int) number;
}

Solution 4
The fourth problem is to create a pile of stones with a given number of levels. The number of stones in each level is the next odd number if the number of levels is odd, and the next even number if the number of levels is even. This can be done by using a loop to calculate the number of stones in each level.
public List<Integer> makeAPile(int n) {
    List