bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            float diff = abs(numbers[i] - numbers[j]);
            if (diff < threshold) {
                return true;
            }
        }
    }
    return false;
}

Explanation:
The function `has_close_elements` takes a vector of floating point numbers and a threshold as input. It iterates over each pair of numbers in the vector and checks if the absolute difference between them is less than the given threshold. If it finds such a pair, it immediately returns `true`. If it doesn't find any pair with a difference less than the threshold, it returns `false`.

In the given examples, the function correctly returns the expected results. For the first example, it returns `false` because no two numbers are closer than 0.5. For the second example, it returns `true` because the numbers 2.0 and 2.8 are closer than 0.3.