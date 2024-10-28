
This is the first time I've seen a question that asks for a review of my solution, so here it goes:
Q1:

The code is correct but can be optimized. Instead of using nested for loops, you can sort the list and then iterate through it once, checking the difference between each element and the next one. This will reduce the time complexity from O(n^2) to O(n log n).
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    Collections.sort(numbers);
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (numbers.get(i + 1) - numbers.get(i) < threshold) {
