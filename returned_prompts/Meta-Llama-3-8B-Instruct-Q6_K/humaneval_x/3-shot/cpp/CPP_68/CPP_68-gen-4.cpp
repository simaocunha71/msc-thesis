    int smallest_value;
    int smallest_index;
    int min_even_value = INT_MAX;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < min_even_value) {
            min_even_value = arr[i];
            smallest_value = arr[i];
            smallest_index = i;
        }
    }
    if (min_even_value == INT_MAX) {
        return {};
    }
    return {smallest_value, smallest_index};
}

