    public List<Double> rescaleToUnit(List<Double> numbers) {
        if (numbers.size() < 2) {
            throw new RuntimeException("List must contain at least two elements");
        }
        // find the min and max values
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        // create a new list and rescale the values
        List<Double> result = new ArrayList<>();
        for (double num : numbers) {
            result.add((num - min) / (max - min));
        }
        return result;
    }

Explanation:
The solution first checks if the list has at least two elements. If not, it throws an exception.
Then it finds the minimum and maximum values in the list using the `Collections.min()` and `Collections.max()` methods.
Finally, it creates a new list and rescales each value by subtracting the minimum value and dividing by the range (maximum - minimum).
This ensures that the smallest value becomes 0 and the largest value becomes 1. The resulting list is then returned.