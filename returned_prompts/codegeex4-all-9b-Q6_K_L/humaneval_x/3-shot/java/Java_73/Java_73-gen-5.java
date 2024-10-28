
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

This is an O(n^2) solution. You can improve it to O(n) by sorting the array first. Then, you can iterate through the array once, and for each element, check if the difference to the next element is smaller than the threshold. If it is, return true. If you reach the end of the array without finding a pair of numbers closer than the threshold, return false.

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

This is a good solution. You could improve it by removing the if statement at the end of the for loop. Instead, you could initialize current_depth to -1, and set it to 0 at the beginning of the for loop. This way, you don't need to check if current_depth is 0 at the end of the loop.

public double truncateNumber(double number) {
    return number % 1.0;
}

This is a good solution. You could improve it by using the Math.floor() method instead of the modulus operator. This way, you don't need to cast the result to a double.

public int smallestChange(List<Integer> arr) {
    int count = 0;
    for (int i = 0, j = arr