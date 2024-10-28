
I'll answer just the first one, as the rest are very similar.
Your first function is basically fine, but there's a few improvements you can do:

Instead of manually iterating through all the numbers, you can use a more efficient algorithm, the two-pointer technique, to find the closest pair of numbers. This will significantly improve performance for large vectors.

You don't need to use a label to break out of the loop. You can use a boolean variable to store the result.

You don't need to use abs. The subtraction of two numbers will give a positive or negative result, and abs doesn't do anything useful here.

You don't need to use int for i and j. You can use size_t, which is the type of the size() function.

Here's the improved code:
bool has_close_elements(const vector<float>& numbers, float threshold) {
    size_t size = numbers.size();
    for (size_t i = 0; i < size - 1; ++i) {
        for (size_t j = i + 1; j < size; ++j) {
            float diff = numbers[i] - numbers[j];
            if (diff < 0) {
                diff = -diff;
            }
            if (diff < threshold) {
                return true;
            }
        }
    }
    return false;
}