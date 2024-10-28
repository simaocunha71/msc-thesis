
I'll start with the last one, because it's the simplest of the three.

chooseNum(int x, int y)

I would suggest renaming x and y to left and right to make it clear what they represent. The name x and y can be confusing in this context because it's usually used for the coordinates of a point in 2D space.
Also, there is no need to use the keyword int before the return type of the method. The return type is already clear from the method name.
Here is the improved version of the method:

public int chooseNum(int left, int right) {
    if (left > right) return -1;
    if (left % 2 == 0) return left;
    if (right % 2 == 0) return right;
    return left + 1;
}

truncateNumber(double number)

This method is fine, but you could simplify it by using the Math.floor() method to get the integer part of the number and then subtracting it from the original number to get the decimal part.

public double truncateNumber(double number) {
    return number - Math.floor(number);
}

separateParenGroups(String paren_string)

This method is a bit more complex and could be improved by adding some comments to explain what each part of the code does. Also, you could use a more descriptive name for the StringBuilder variable, such as currentGroup.
Here is the improved version of the method:

public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    StringBuilder currentGroup = new StringBuilder();
    int currentDepth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            currentDepth += 1;
            currentGroup.append(c);
        } else if (c == ')') {
            currentDepth -= 1;
            currentGroup.append(c);

            if (currentDepth == 0) {
                result.add(currentGroup.toString());
                currentGroup.setLength(0);
            }
        }
    }
    return result;
}

hasCloseElements(List<Double> numbers, double threshold)

This method could be improved by using a more descriptive name for the variable threshold, such as distanceThreshold. Also, you could simplify the code by using