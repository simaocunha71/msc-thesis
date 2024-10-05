
I see you've got some work to do on your code. I'll get you started on the first one, then I'll leave you to the rest.
Problem 1: Check if in given list of numbers, are any two numbers closer to each other than given threshold.

The first thing to do is to sort the list. That way, the closest two numbers will always be next to each other. However, you're required to find out if two numbers are closer than a threshold, and not to find the closest two numbers. So, you need to iterate through the list in pairs and check if the difference between each pair is less than the threshold.
Here's how you can do it:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Collections.sort(numbers);
    for (int i = 1; i < numbers.size(); i++) {
        double difference = Math.abs(numbers.get(i) - numbers.get(i - 1));
        if (difference < threshold) {
            return true;
        }
    }
    return false;
}

Problem 2: Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those group into separate strings and return the list of those.

You're already doing a good job with this one, but you have a couple of problems. First, you're not ignoring spaces in the input string. Second, you're not handling the case where there are no parentheses in the input string. Here's a modified version of your code that addresses these issues:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();
    int current_depth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(' || c == ' ') {
            current_depth += 1;
            current_string.append(c);
        } else if (c == ')') {
            current_depth -= 1;
            current_string.append(c);

            if (current_depth == 0) {
                result.add(current_string.toString().replaceAll("