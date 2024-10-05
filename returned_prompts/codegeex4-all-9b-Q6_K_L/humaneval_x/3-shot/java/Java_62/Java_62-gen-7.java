
You have the right idea in the first problem, but you can make the code a little more efficient by reducing the number of iterations.  This will also make your code a bit more readable.  Instead of starting your inner loop at i + 1, you can start it at 0, and then add i to j in your loop.  This will make the code look like this:
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = 0; j < numbers.size(); j++) {
            if (i != j) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
            }
        }
    }
    return false;
}

Your second problem is also correct, but you can make it more efficient by using a stack to keep track of the depth of the parentheses.  This will make the code look like this:
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

Your third problem is also correct, but you can make it more efficient by using a loop to iterate through the list of coefficients.  This will make the code look like this:
public List<Integer> derivative(List<Integer> xs) {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < xs.size() - 1; i++) {
        result.add(xs.get(i + 1) * (i + 1));
    }
    return result;
}

Overall, you have the right idea for all three problems, but you can