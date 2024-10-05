
The first question is easy. You just need to iterate over the List<Double> and keep track of the smallest difference between any two elements.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Double last = null;
    for (Double n : numbers) {
        if (last != null && Math.abs(last - n) < threshold) {
            return true;
        }
        last = n;
    }
    return false;
}

The second question is also easy. You just need to iterate over the String, and keep track of the current depth of parentheses, as well as the current group of parentheses.
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    int depth = 0;
    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            depth++;
            current.append(c);
        } else if (c == ')') {
            depth--;
            current.append(c);
            if (depth == 0) {
                result.add(current.toString());
                current.setLength(0);
            }
        }
    }
    return result;
}

The third question is a bit more complicated. You need to truncate the number to the nearest integer, and then return the difference between the original number and the truncated number.
public double truncateNumber(double number) {
    return number - Math.floor(number);
}

The fourth question is also a bit more complicated. You need to create a HashMap to store the frequency of each letter, and then iterate over the HashMap to find the letter(s) with the highest frequency.
public Map<String, Integer> histogram(String test) {
    Map<String, Integer> result = new HashMap<>();
    String[] words = test.split(" ");
    for (String word : words) {
        if (result.containsKey(word)) {
            result