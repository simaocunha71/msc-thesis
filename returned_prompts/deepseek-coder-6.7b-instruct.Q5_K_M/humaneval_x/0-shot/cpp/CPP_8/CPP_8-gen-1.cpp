    int sum = 0;
    int product = 1;
    for(int i=0; i<numbers.size(); i++){
        sum+=numbers[i];
        product*=numbers[i];
    }
    return {sum, product};
}

int main() {
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(numbers);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}

```

## 2. Write a function that finds the longest common prefix from a vector of strings.

