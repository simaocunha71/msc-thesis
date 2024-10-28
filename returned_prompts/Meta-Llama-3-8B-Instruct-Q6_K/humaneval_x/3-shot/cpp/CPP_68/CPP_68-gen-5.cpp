    int smallest = INT_MAX, index = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < smallest) {
            smallest = arr[i];
            index = i;
        }
    }
    if (index == -1) {
        return {};
    }
    return {smallest, index};
}