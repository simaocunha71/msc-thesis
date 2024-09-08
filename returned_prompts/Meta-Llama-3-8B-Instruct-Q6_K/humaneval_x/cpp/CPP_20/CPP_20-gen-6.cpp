    // Find the smallest number
    float min = *min_element(numbers.begin(), numbers.end());
    // Find the largest number
    float max = *max_element(numbers.begin(), numbers.end());
    // Find the closest number to the smallest
    float closest_to_min = *min_element(numbers.begin(), numbers.end(), 
 [](float a, float b){return abs(a - min) < abs(b - min);});
    // Find the closest number to the largest
    float closest_to_max = *min_element(numbers.begin(), numbers.end(), 
 [](float a, float b){return abs(a - max) < abs(b - max);});

    // Return the closest numbers
    return {closest_to_min, closest_to_max};
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> closest_pair = find_closest_elements(numbers);
    printf("(%.2f, %.2f)\n", closest_pair[0], closest_pair[1]);
    return 0;
}
```

