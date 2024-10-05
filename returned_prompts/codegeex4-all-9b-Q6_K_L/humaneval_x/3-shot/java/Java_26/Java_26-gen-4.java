
The first question is asking to determine if any two numbers in a list are within a specified threshold of each other. 
Your code is on the right track, but it's a bit overcomplicated. You don't need to use two loops - you can just iterate through the list once, and for each element, compare it to all the elements that come after it. If you find any that are within the threshold, you can return true immediately. If you go through the whole list without finding any, you can return false. 
Here's a simpler version of your code:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

The second question is asking to separate groups of parentheses from a given string. 
Your code is also on the right track, but it's a bit overcomplicated. You don't need to keep track of the current depth or use a StringBuilder. You can just iterate through the string character by character, and whenever you encounter an opening parenthesis, you can add it to a list. When you encounter a closing parenthesis, you can remove the last opening parenthesis from the list and add the current substring (from the last opening parenthesis to the current closing parenthesis) to a result list. 
Here's a simpler version of your code:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    List<Integer> open_paren_indices = new ArrayList<>();

    for (int i = 0; i < paren_string.length(); i++) {
        char c = paren_string.charAt(i);
        if (c == '(') {
            open_paren_indices.add(i);
        } else if (c == ')') {
            if (open_paren_indices.isEmpty()) {
                throw new IllegalArgumentException("Unbalanced parentheses");
            }
            int start_index = open_paren_indices.remove(open_paren_indices.size() - 1);
            result.add(paren_string.substring(start_index, i + 1));
        }
    }

    if (!open_paren_indices.isEmpty()) {
        throw new IllegalArgumentException("Unbalanced parentheses");
    }

    return result