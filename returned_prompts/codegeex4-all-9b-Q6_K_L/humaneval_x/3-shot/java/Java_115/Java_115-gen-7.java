
In the first example, you can simplify the condition to:
if (distance < threshold) {
    return true;
}

In the second example, you can simplify the logic a bit:
List<String> result = new ArrayList<>();
StringBuilder current_string = new StringBuilder();
int current_depth = 0;

for (char c : paren_string.toCharArray()) {
    if (c == '(') {
        current_depth += 1;
    } else if (c == ')') {
        current_depth -= 1;

        if (current_depth == 0) {
            result.add(current_string.toString());
            current_string.setLength(0);
        }
    }
    current_string.append(c);
}
return result;

In the third example, you can simplify the logic a bit:
public double truncateNumber(double number) {
    return number - (int) number;
}

In the fourth example, you can simplify the logic a bit:
public int maxFill(List<List<Integer>> grid, int capacity) {
    int max_fill = 0;
    for (List<Integer> row : grid) {
        for (int i = 0; i < row.size(); i++) {
            if (row.get(i) == 1) {
                max_fill += 1;
                row.set(i, 0);
                int fill = 1;
                while (fill < capacity && i + fill < row.size() && row.get(i + fill) == 1) {
                    fill += 1;
                    row.set(i + fill, 0);
                }
            }
        }
    }
    return max_fill;
}