    vector<float> result;
    float min_val = *min_element(numbers.begin(), numbers.end());
    float max_val = *max_element(numbers.begin(), numbers.end());
    for (float num : numbers) {
        result.push_back((num - min_val) / (max_val - min_val));
    }
    return result;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> result = rescale_to_unit(numbers);
    for (float num : result) {
        printf("%f ", num);
    }
    printf("\n");
    return 0;
}

O/P:
0.000000 0.250000 0.500000 0.750000 1.000000 

Explanation:
In the above code, the function rescale_to_unit takes a vector of floating point numbers as input. It calculates the minimum and maximum values in the vector. Then it iterates over the input vector, subtracts the minimum value from each number, and divides the result by the difference between the maximum and minimum values. This operation rescales the input numbers to be in the range [0, 1]. The resulting vector is returned by the function.

In the main function, a sample vector of numbers is created, and the rescale_to_unit function is called with this vector as input. The result is then printed to the console. The output shows the rescaled numbers, which are in the range [0, 1]. The smallest number in the input vector (1.0) is mapped to 0.0, and the largest number (5.0) is mapped to 1.0. The other numbers are mapped linearly between these two extremes. 

This operation is commonly used in data preprocessing and normalization, as it helps to reduce the effect of extreme values in the data and can improve the performance of machine learning algorithms. It is also used in data visualization, as it helps to make the data more visually appealing and easier to understand. 