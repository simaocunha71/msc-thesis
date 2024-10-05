    int sum = array[0] + array[array.size()-1];
    if (sum%2 == 0) {
        sort(array.begin(), array.end(), greater<int>());
    } else {
        sort(array.begin(), array.end());
    }
    return array;
}

int main(void) {
    vector<int> array = {2, 4, 3, 0, 1, 5};
    vector<int> result = sort_array(array);
    for (auto i : result) {
        printf("%d ", i);
    }
    return 0;
}
