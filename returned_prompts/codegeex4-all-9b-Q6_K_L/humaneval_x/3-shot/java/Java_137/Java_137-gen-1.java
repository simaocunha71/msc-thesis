
You have a lot of similar code, which is easy to refactor. I'll show you how to do it with the first example. Let me know if you want me to do the rest.

public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
