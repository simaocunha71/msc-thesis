
hasCloseElements
Your code is correct, and it's pretty good style. There are a few small things that could be improved:

You're using a for-loop with an index, which is fine, but there are other ways to loop through a list in Java:

You could use an enhanced for-loop, which is more concise:
for (Double number : numbers) { ... }

You could use Java 8's streams, which is more functional in style:
numbers.stream().anyMatch((number1, number2) -> Math.abs(number1 - number2) < threshold);

This is more complex, but it's a good example of a more functional style of programming.

separateParenGroups
Your code is also correct, and it's pretty good style. There are a few small things that could be improved:

You're using a StringBuilder to build the current string, which is fine, but you're also calling toString() and setLength(0) on it. You could use a String instead, which is simpler:
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

You could use a for-each loop to loop through the characters in the string, which is more concise:
for (char c : paren_string.toCharArray()) { ... }

truncateNumber
Your code is also correct, and it's pretty good style. There are a few small things that could be improved:

You're using a float constant, which is fine, but you could use a double constant instead:
return number % 1.0;

sameChars
Your code is also correct, and it's pretty good style. There are a few small things that could be improved:

You're using a for-loop with an index, which is fine, but there are other ways to loop through a list in Java:

You could use an enhanced for-loop, which