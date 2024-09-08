    if (numbers.empty()) {
        return {0, 1};
    }
    int sum = 0;
    int product = 1;
    for (int i : numbers) {
        sum += i;
        product *= i;
    }
    return {sum, product};
}
int main() {
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(numbers);
    printf("Sum: %d\n", result[0]);
    printf("Product: %d\n", result[1]);
    return 0;
}

