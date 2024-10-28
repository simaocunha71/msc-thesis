
Your questions are interesting, but the answers are a bit confusing.  For the first question, you have a nested for loop that checks every pair of numbers in the list to see if they are within the threshold of each other.  This is a good way to do it.  However, there is a more efficient way to do it using the Collections.sort() method.  Here's how it would look:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Collections.sort(numbers);
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (numbers.get(i + 1) - numbers.get(i) < threshold) {
            return true;
        }
    }
    return false;
}

This sorts the list of numbers in ascending order, and then checks every pair of adjacent numbers to see if they are within the threshold of each other.  If any pair of numbers is within the threshold, it returns true.  If it goes through the entire list and doesn't find any pair of numbers within the threshold, it returns false.
For the second question, you are trying to separate groups of parentheses in a string.  You are doing a good job with the current_depth variable, but you don't need to append each character to the current_string as you go.  Instead, you can just keep track of the current_depth and add the parentheses to the result list when the current_depth is 0.
Here's how it would look:
public List<String> separateParenGroups(String paren_string) {
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
                current_string.setLength(0