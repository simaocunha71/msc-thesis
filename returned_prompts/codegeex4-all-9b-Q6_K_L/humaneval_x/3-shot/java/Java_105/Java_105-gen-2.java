
The first question has a bug. You are checking for pairs of numbers within the same list, not in different lists.
Here is the correct code:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    List<Double> numbersCopy = new ArrayList<>(numbers);
    for (int i = 0; i < numbers.size(); i++) {
        Double num = numbers.get(i);
        numbersCopy.remove(num);
        for (int j = 0; j < numbersCopy.size(); j++) {
            Double num2 = numbersCopy.get(j);
            if (Math.abs(num - num2) < threshold) {
                return true;
            }
        }
    }
    return false;
}

The second question is about separating groups of parentheses. The code is correct, but it is not very efficient. You can use a stack to solve this problem in O(n) time complexity.
Here is the correct code:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();
    Stack<Character> stack = new Stack<>();

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            stack.push(c);
            current_string.append(c);
        } else if (c == ')') {
            stack.pop();
            current_string.append(c);

            if (stack.isEmpty()) {
                result.add(current_string.toString());
                current_string.setLength(0);
            }
        }
    }
    return result;
}

The third question is about truncating a number. The code is correct, but it can be simplified by using the Math.floor() function.
Here is the correct code:
public double truncateNumber(double number) {
    return Math.floor(number);
}

The fourth question is about sorting and reversing an array of integers. The code is correct, but it can be simplified by using a custom Comparator.
Here is the correct code:
public List<String> byLength(List<Integer> arr) {
    List<String> result = new ArrayList<>();
    String[] names = {"One", "Two