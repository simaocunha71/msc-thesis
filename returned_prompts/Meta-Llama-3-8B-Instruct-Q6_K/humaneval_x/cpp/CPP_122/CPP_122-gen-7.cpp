    int sum = 0;
    for (int i = 0; i < k; i++) {
        if (abs(arr[i]) < 100) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d",add_elements(arr,k));
    return 0;
}