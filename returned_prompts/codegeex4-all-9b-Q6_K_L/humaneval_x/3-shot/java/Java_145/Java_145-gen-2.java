
I have a few comments for each of your methods:

hasCloseElements:

There's no need to use Math.abs() on a double value that's already a positive number. You can simply use the subtraction result directly. This can be done using a lambda for a more modern approach:

    return IntStream.range(0, numbers.size())
                    .anyMatch(i -> IntStream.range(i + 1, numbers.size())
 .anyMatch(j -> numbers.get(i) - numbers.get(j) < threshold));

separateParenGroups:

You don't need to check for a current_depth of 0. You can instead check for a current_depth of 1 (the first opening parenthesis) and then check for a closing parenthesis. This can be done using a flag to check whether you're currently in a group or not:

    List<String> result = new ArrayList<>();
    StringBuilder current_string = new StringBuilder();
    boolean in_group = false;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_string.append(c);
            in_group = true;
        } else if (c == ')') {
            current_string.append(c);
            in_group = false;
        }
        if (!in_group && current_string.length() > 0) {
            result.add(current_string.toString());
            current_string.setLength(0);
        }
    }
    return result;

truncateNumber:

You don't need to use 1.0 as the divisor. You can simply use 1. This can be done using a lambda for a more modern approach:

    return number % 1;

orderByPoints:

You don't need to use a lambda for the comparator. You can instead use the Comparator.comparingInt() method:

    Collections.sort(nums, Comparator.comparingInt(a -> {
        int sum = 0;
        while (a != 0) {
            sum += a % 10;
            a /= 10;
        }
