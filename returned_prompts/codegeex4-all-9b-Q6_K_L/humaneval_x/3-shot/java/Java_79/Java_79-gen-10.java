
I am going to make some assumptions and provide a solution for the first question. If you have any questions, please ask. I will assume that the list of numbers will have at least one number.
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}

This code iterates over all pairs of numbers in the list and calculates the absolute difference between them. If the difference is less than the threshold, the function returns true. If no such pair is found, the function returns false.