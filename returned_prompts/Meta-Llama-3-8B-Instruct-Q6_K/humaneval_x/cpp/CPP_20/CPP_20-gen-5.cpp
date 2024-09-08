    vector<float> closest_elements = numbers;
    float min_diff = numeric_limits<float>::max();
    float closest1 = 0;
    float closest2 = 0;

    for(int i = 0; i < numbers.size(); i++) {
        for(int j = i+1; j < numbers.size(); j++) {
            float diff = abs(numbers[i] - numbers[j]);
            if(diff < min_diff) {
                min_diff = diff;
                closest1 = numbers[i];
                closest2 = numbers[j];
            }
        }
    }
    return {closest1, closest2};
}

int main()
{
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> closest = find_closest_elements(numbers);
    cout << "(" << closest[0] << ", " << closest[1] << ")" << endl;
    return 0;
}

Explanation:
This C++ program defines a function `find_closest_elements` that takes a vector of floating-point numbers as input and returns a vector containing the two numbers in the input vector that are closest to each other.

The function iterates over each pair of numbers in the input vector using two nested loops. For each pair of numbers, it calculates the absolute difference between the two numbers. If the difference is less than the current minimum difference, it updates the minimum difference and the closest numbers.

Finally, the function returns a vector containing the two closest numbers.

In the `main` function, we create a vector of floating-point numbers and call the `find_closest_elements` function to find the closest pair of numbers. We then print the result to the console.

The time complexity of this function is O(n^2), where n is the size of the input vector, because it uses two nested loops to iterate over each pair of numbers. The space complexity is O(1), because it only uses a constant amount of space to store the minimum difference and the closest numbers.