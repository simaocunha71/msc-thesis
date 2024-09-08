    // calculate the smallest and largest numbers
    float min_val = *min_element(numbers.begin(), numbers.end());
    float max_val = *max_element(numbers.begin(), numbers.end());

    // calculate the linear transform
    for (float &num : numbers) {
        num = (num - min_val) / (max_val - min_val);
    }

    return numbers;
}  // end of function rescale_to_unit

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> rescaled_numbers = rescale_to_unit(numbers);

    for (float num : rescaled_numbers) {
        printf("%f ", num);
    }
    printf("\n");

    return 0;
} // end of main

O/P:
0.000000 0.250000 0.500000 0.750000 1.000000

Explanation:
* We first find the smallest and largest numbers in the vector.
* Then we apply a linear transform to each number, by subtracting the smallest number and then dividing by the difference between the largest and smallest numbers.
* This effectively scales the numbers to be between 0 and 1.
* Finally, we return the rescaled vector.
* In the main function, we create a vector of numbers, rescale it using the rescale_to_unit function, and then print the result.