    vector<int> max_numbers;
    int max_value = numbers[0];
    for(auto i=0; i<numbers.size(); i++){
        if (numbers[i] > max_value)
            max_value = numbers[i];
        max_numbers.push_back(max_value);
    }
    return max_numbers;
}
int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> max_numbers = rolling_max(numbers);
    for(auto i=0; i<max_numbers.size(); i++){
        printf("%d ", max_numbers[i]);
    }
    return 0;
}

*/

This is a C++ solution which works by iterating over the vector of integers and keeping track of the maximum value found so far. The maximum value is then pushed back onto the result vector.

This solution has a time complexity of O(n) because it iterates over the vector once, and a space complexity of O(n) because it creates a new vector to store the results.

Here is a Python solution using a similar approach:

```python
def rolling_max(numbers):
    max_numbers = []
    max_value = numbers