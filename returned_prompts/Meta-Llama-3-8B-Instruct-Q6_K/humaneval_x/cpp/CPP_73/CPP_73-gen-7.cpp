    int n = arr.size();
    vector<int> left(n, 0), right(n, 0);
    int res = 0;

    for (int i = 0; i < n; i++) {
        if (i > 0) {
            left[i] = left[i - 1];
        }
        if (i < n - 1) {
            right[i] = right[i + 1];
        }
        if (arr[i] == arr[n - i - 1]) {
            left[i]++;
            right[n - i - 1]++;
        }
        res += min(n - 1 - left[i], right[i]);
    }
    return res;
}

int main() {
    vector<int> arr = {1,2,3,5,4,7,9,6};
    cout << smallest_change(arr) << endl;
    return 0;
}
