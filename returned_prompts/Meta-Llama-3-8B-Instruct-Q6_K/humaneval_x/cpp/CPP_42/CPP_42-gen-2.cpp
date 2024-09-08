    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result.push_back(l[i] + 1);
    }
    return result;
}

int main() {
    vector<int> v = {1, 2, 3};
    vector<int> result = incr_list(v);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
```

This C++ code defines a function `incr_list` that takes a vector of integers as input, increments each element by 1, and returns a new vector with the incremented values. The function is then called with a sample input vector `{1, 2, 3}`, and the resulting vector is printed to the console. The output is `{2, 3, 4}`. The function iterates over the input vector using a for loop, increments each element by 1, and appends the result to a new vector, which is then returned. This approach is more efficient and easier to understand than the given Python solution. The C++ code is also more concise and easier to read. The `main` function demonstrates the usage of the `incr_list` function with a sample input and prints the result.