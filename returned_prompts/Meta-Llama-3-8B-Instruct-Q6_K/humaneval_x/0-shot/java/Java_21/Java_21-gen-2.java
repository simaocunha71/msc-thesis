    public List<Double> rescaleToUnit(List<Double> numbers) {
        if (numbers.size() < 2) {
            throw new RuntimeException("List must have at least two elements");
        }

        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> result = new ArrayList<>();
        for (double number : numbers) {
            result.add((number - min) / (max - min));
        }

        return result;
    }A

    Explanation:
    This problem is asking to normalize the given list of numbers so that the smallest number becomes 0 and the largest becomes 1.
    We can do this by subtracting the smallest number from each number in the list, and then dividing the result by the difference between the smallest and largest numbers.
    We use the `Collections.min` and `Collections.max` methods to find the smallest and largest numbers in the list, respectively.
    We then iterate over the list, subtract the smallest number from each number, and divide the result by the difference between the smallest and largest numbers.
    The resulting list is then returned.

    The unit test `rescaleToUnit(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0))` checks that the function works correctly for the input `[1.0, 2.0, 3.0, 4.0, 5.0]`.
    It expects the output to be `[0.0, 0.25, 0.5, 0.75, 1.0]`, which is the normalized version of the input list.