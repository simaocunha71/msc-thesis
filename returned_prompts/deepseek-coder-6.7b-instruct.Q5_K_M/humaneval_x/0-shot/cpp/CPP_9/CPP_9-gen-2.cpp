    vector<int> result;
    int max_num = numbers[0];
    result.push_back(max_num);
    for (int i = 1; i < numbers.size(); i++){
        if (numbers[i] > max_num){
            max_num = numbers[i];
        }
        result.push_back(max_num);
    }
    return result;
}

int main(){
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for (int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}
```

### Explanation:

The problem is to find the maximum value in the array until the current index.

In the C++ code, we are creating a vector named `result`. We first add the first element of the array to the `result`. Then we loop through the array from the second element. In each iteration, we check if the current element is greater than the maximum number found so far. If it is, we update the maximum number. We then add the maximum number to the `result`.

Finally, we return the `result` vector.

The `main` function prints the elements of the `result` vector.

This C++ code will output:

```
1 2 3 3 3 4 4
```

which is the rolling maximum of the given array.

### Complexity Analysis:

Time Complexity: The time complexity of this code is O(n), where n is the size of the input array. We are performing a single pass through the array.

Space Complexity: The space complexity of this code is also O(n), where n is the size of the input array. We are storing the result in a new array.

### Notes:

This solution assumes that the input vector is not empty. If the input vector can be empty, the code should be modified to handle this case.

The code uses C++ standard library, so it should be compiled with a C++ compiler.

The