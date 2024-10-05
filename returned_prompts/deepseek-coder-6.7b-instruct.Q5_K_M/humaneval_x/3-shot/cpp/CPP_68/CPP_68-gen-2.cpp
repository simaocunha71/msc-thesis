    int smallest_even_value = INT_MAX;
    int smallest_even_index = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] < smallest_even_value && arr[i] % 2 == 0) {
            smallest_even_value = arr[i];
            smallest_even_index = i;
        }
    }
    if (smallest_even_index == -1) {
        return {};
    } else {
        return {smallest_even_value, smallest_even_index};
    }
}


