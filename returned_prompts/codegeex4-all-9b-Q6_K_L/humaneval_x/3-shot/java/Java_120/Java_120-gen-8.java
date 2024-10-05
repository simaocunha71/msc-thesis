
public boolean hasCloseElements(List<Double> numbers, double threshold)

The parameter names could be more descriptive.
What is a "threshold"?
Does it mean "tolerance"?
If so, what does the function return when there are no "close elements"?
Is it true or false?
What does the function return when there are "close elements"?
Is it true or false?
What does the function return when there is only one number in the list?
Is it true or false?

I would rename the function to something like "hasElementsWithinTolerance" and the parameter to something like "tolerance".
public boolean hasElementsWithinTolerance(List<Double> numbers, double tolerance)

I would rename the variables to something like:
for (int index = 0; index < numbers.size(); index++) {
    for (int nextIndex = index + 1; nextIndex < numbers.size(); nextIndex++) {
        double distance = Math.abs(numbers.get(index) - numbers.get(nextIndex));
        if (distance < tolerance) return true;
    }
}

I would also consider using a HashSet to check if the list contains duplicate values. If it does, then the function could immediately return true.
If the list doesn't contain duplicate values, then the function could return false.
public boolean hasElementsWithinTolerance(List<Double> numbers, double tolerance) {
    Set<Double> uniqueValues = new HashSet<>(numbers);
    if (uniqueValues.size() < numbers.size()) return true;
    for (int index = 0; index < numbers.size(); index++) {
        for (int nextIndex = index + 1; nextIndex < numbers.size(); nextIndex++) {
            double distance = Math.abs(numbers.get(index) - numbers.get(nextIndex));
            if (distance < tolerance) return true;
        }
    }
    return false;
}

public List<String> separateParenGroups(String paren_string)

The parameter name could be more descriptive.
What is a "