    int sum = 0;
    for (int i = 0; i < k; i++) {
        if (log10(arr[i]) + 1 <= 2) {
            sum += arr[i];
        }
        else {
            break;
        }
    }
    return sum;
}

int main() {
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d", add_elements(arr,k));
    return 0;
}

