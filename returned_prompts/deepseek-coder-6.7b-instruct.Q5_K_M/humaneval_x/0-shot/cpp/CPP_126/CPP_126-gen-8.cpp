    for(int i=0; i<lst.size()-1; i++){
        if(lst[i]>=lst[i+1]){
            return false;
        }
    }
    return true;
}

int main()
{
    vector<int> a = {1, 2, 3, 4, 5};
    printf(is_sorted(a) ? "true" : "false");
    return 0;
}
```

In the given code, we declare a function `is_sorted` that takes a vector of integers as input and returns a boolean value indicating whether the input vector is sorted in ascending order. If the vector is sorted, the function returns `true`, otherwise it returns `false`.

The function uses a for loop to iterate over the elements of the vector. It compares each element with the next one. If any element is greater than or equal to the next one, the function immediately returns `false` because the vector is not sorted. If the function completes the loop without finding any such pair, it returns `true` indicating that the vector is sorted.

Finally, in the `main` function, we test the `is_sorted` function with a vector `a` and print the result.

The output for the given vector `a` should be `true`.

```
true
```

Please note that this solution assumes that the input vector does not contain any negative numbers and only contains integers. If the input can contain negative numbers, you will need to modify the comparison condition in the for loop to `lst[i]>lst[i+1]`.

Also, this solution assumes that the vector does not have more than one duplicate of the same number. If the vector can have duplicates, you will need to modify the function to count the occurrences of each number and return `false` if more than one number has duplicates.
