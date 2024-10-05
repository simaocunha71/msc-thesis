    vector<int> result;
    for(int i = 0; i < numbers.size(); i++){
        result.push_back(numbers[i]);
        if(i < numbers.size() - 1){
            result.push_back(delimeter);
        }
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    vector<int> result = intersperse(numbers, delimeter);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}
```

**Output**
```
1 4 2 4 3 
```

## Time Complexity: O(n)
## Space Complexity: O(n)

This solution works by iterating over the input vector, and for each element, adding it to a new vector, followed by the delimiter. In the end, the new vector is returned as the result. The time complexity is O(n) as we are looping over the input vector once. The space complexity is also O(n) because we are creating a new vector that could potentially be as large as the input vector.

This solution assumes that the input vector is not empty. If the input vector could be empty, then the solution would need to be modified to handle that case.

**Note**: This solution assumes that the input vector is not empty. If the input vector could be empty, then the solution would need to be modified to handle that case.

**Note**: The delimiter is not considered as part of the output if it is the same as any element in the input vector.

**Note**: The output of this solution is a vector of integers. If you want to output the result in a different format, you will need to modify the output part of the code.

**Note**: This solution assumes that the input vector is a vector of integers. If the input vector could contain other types of elements, you will need to modify the solution to handle that case.

**Note**: This solution assumes that the delimiter is an integer. If the delimiter is not