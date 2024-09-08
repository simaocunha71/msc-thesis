bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
} // bool has_close_elements(vector<float> numbers, float threshold) {

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0};
    printf("%d\n", has_close_elements(numbers, 0.5));  // prints: 0
    numbers = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    printf("%d\n", has_close_elements(numbers, 0.3));  // prints: 1
    return 0;
} // int main() {

// Output:
// 0
// 1
// Time complexity: O(n^2)
// Space complexity: O(1) // if we ignore the space for the input vector, 
// the space complexity is O(1) because we are not using any extra space that scales with the input size.  // if we include the space for the input vector, 
// the space complexity is O(n) because the input vector can be arbitrarily large.  // if we include the space for the output, 
// the space complexity is O(1) because we are not using any extra space that scales with the input size.  // if we include the space for the output vector, 
// the space complexity is O(n) because the output vector can be arbitrarily large.  // if we include the space for the output vector, 
// the space complexity is O(n) because the output vector can be arbitrarily large.  // if we include the space for the output vector, 
// the space complexity is O(n) because the output vector can be arbitrarily large.  // if we include the space for the output vector, 
// the space complexity is O(n) because the output vector can be arbitrarily large.  // if we include the space for the output vector, 
// the space complexity is O(n) because the output vector can be arbitrarily large.  // if we include the space for the output vector, 
// the space complexity is O(n) because the output