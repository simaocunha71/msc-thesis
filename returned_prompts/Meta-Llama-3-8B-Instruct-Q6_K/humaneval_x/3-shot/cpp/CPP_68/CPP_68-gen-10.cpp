    int smallest = INT_MAX, smallest_index = -1;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] % 2 == 0 && arr[i] < smallest) {
            smallest = arr[i];
            smallest_index = i;
        }
    }
    if(smallest_index == -1) {
        return {};
    }
    return {smallest, smallest_index};
}  // End of function pluck


