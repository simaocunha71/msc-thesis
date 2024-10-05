
hasCloseElements
This is an O(n^2) solution because you are using a nested loop. You can make this O(n) by sorting the numbers first and then checking for numbers within threshold distance.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Collections.sort(numbers);
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (numbers.get(i + 1) - numbers.get(i) < threshold) {
            return true;
        }
    }
    return false;
}

separateParenGroups
The logic here is correct, but the variable names could be better. current_string and current_depth are not very descriptive. I would suggest using something like current_group and group_depth.
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_group = new StringBuilder();
    int group_depth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            group_depth += 1;
            current_group.append(c);
        } else if (c == ')') {
            group_depth -= 1;
            current_group.append(c);

            if (group_depth == 0) {
                result.add(current_group.toString());
                current_group.setLength(0);
            }
        }
    }
    return result;
}

truncateNumber
This is a straightforward implementation of the problem. However, you could make it more efficient by using the Math.floor method instead of calculating the modulus.
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

getOddCollatz
This is a correct implementation of the Collatz sequence, but it could be more efficient. You could use a HashSet to keep track of the numbers you have already seen, and if you encounter a number you have already seen, you can stop the loop.
public List<Integer> getOddCollatz(int n) {
    Set<Integer> seen = new HashSet<>();
    List<Integer