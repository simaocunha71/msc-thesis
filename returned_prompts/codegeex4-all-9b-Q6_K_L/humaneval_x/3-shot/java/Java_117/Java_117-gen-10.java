
for (int i = 0; i < numbers.size(); i++) {
    for (int j = i + 1; j < numbers.size(); j++) {
        double distance = Math.abs(numbers.get(i) - numbers.get(j));
        if (distance < threshold) return true;
    }
}
return false;

Your solution works, but you can make it more efficient by sorting the list first. Then, if two numbers are close, they will be next to each other in the sorted list. This way, you only need to check adjacent numbers, not all pairs.

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

Your solution works, but you can make it more efficient by using a stack. This way, you don't need to keep track of the current depth separately.

public double truncateNumber(double number) {
    return number % 1.0;
}

Your solution works, but you can make it more efficient by using integer arithmetic. This way, you don't need to use floating-point arithmetic.

List<String> result = new ArrayList<>();
String[] words = s.split(" ");

for (String word : words) {
    int count = 0;
    for (char c : word.toCharArray()) {
        if (c != 'a' && c != 'e' && c != 'i' && c