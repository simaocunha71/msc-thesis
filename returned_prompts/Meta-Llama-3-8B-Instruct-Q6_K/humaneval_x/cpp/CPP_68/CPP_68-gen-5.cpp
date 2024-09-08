    vector<int> result;
    if (arr.empty()) {
        return result;
    }
    int min_even_value = INT_MAX;
    int min_even_index = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < min_even_value) {
            min_even_value = arr[i];
            min_even_index = i;
        }
    }
    if (min_even_value == INT_MAX) {
        return result;
    }
    result.push_back(min_even_value);
    result.push_back(min_even_index);
    return result;
}

int main() {
    vector<int> arr = {4,2,3};
    vector<int> result = pluck(arr);
    printf("The plucked node is: {%d, %d}\n", result[0], result[1]);
    return 0;
}
