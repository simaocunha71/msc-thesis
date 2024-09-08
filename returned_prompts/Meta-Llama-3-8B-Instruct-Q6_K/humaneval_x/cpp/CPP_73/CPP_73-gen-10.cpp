    int left = 0;
    int right = arr.size() - 1;
    int changes = 0;

    while (left < right) {
        if (arr[left] != arr[right]) {
            changes++;
            right--;
        } else {
            left++;
        }
    }
    return changes;
}

int main() {
    vector<int> arr = {1,2,3,5,4,7,9,6};
    printf("%d\n", smallest_change(arr));
    return 0;
}
