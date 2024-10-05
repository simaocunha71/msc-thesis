    int min_even = 10001;
    int min_even_index = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] < min_even && arr[i] % 2 == 0) {
            min_even = arr[i];
            min_even_index = i;
        }
    }
    if (min_even_index == -1) return {};
    return {min_even, min_even_index};
}

