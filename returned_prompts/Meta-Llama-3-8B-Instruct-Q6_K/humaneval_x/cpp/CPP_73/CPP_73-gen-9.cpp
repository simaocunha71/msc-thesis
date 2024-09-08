    int n = arr.size();
    int res = 0;
    int left = 0, right = n - 1;

    while (left < right) {
        if (arr[left] != arr[right]) {
            res++;
            left++;
        } else {
            left++;
            right--;
        }
    }

    return res;
}

int main() {
    vector<int> arr = {1,2,3,5,4,7,9,6};
    printf("%d\n", smallest_change(arr));
    return 0;
}