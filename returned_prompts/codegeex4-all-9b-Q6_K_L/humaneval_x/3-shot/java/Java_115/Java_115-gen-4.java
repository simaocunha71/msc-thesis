
1.
Your hasCloseElements method seems correct, I would only suggest adding a comment explaining what the method is meant to do.
2.
Your separateParenGroups method seems correct, but you can make it more efficient by removing the current_depth variable. Here's an updated version:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_string.append(c);
        } else if (c == ')') {
            current_string.append(c);
            if (current_string.length() > 0 && current_string.charAt(0) == '(') {
                result.add(current_string.toString());
                current_string.setLength(0);
            }
        }
    }
    return result;
}

3.
Your truncateNumber method seems correct, but you can make it more efficient by using the Math.floor method. Here's an updated version:
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

4.
Your maxFill method seems correct, but you can make it more efficient by using a single loop to count the number of 1's in each row. Here's an updated version:
public int maxFill(List<List<Integer>> grid, int capacity) {
    int result = 0;
    for (List<Integer> row : grid) {
        int current_row = 0;
        for (int col : row) {
            if (col == 1) current_row += 1;
        }
        result += current_row / capacity;
    }
    return result;
}

Overall, your solutions seem correct, but there are some areas where you can improve efficiency and readability.