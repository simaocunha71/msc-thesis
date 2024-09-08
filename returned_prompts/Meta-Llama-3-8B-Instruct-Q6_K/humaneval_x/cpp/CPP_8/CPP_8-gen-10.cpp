    vector<int> result;
    long long sum = 0;
    long long product = 1;
    for (int num : numbers) {
        sum += num;
        product *= num;
    }
    result.push_back(sum);
    result.push_back(product);
    return result;
}
int main() {
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(numbers);
    printf("Sum: %d\n", result[0]);
    printf("Product: %d\n", result[1]);
    return 0;
}
