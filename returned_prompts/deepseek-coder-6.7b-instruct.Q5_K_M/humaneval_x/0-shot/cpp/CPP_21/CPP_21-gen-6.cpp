// Find the max and min elements in the vector
float min = *min_element(numbers.begin(), numbers.end());
float max = *max_element(numbers.begin(), numbers.end());

// Calculate the range of the original data
float range = max - min;

// Rescale each element in the vector
for (int i = 0; i < numbers.size(); i++){
    numbers[i] = (numbers[i] - min) / range;
}

return numbers;


