    int sum = 0;
    for(int i=0; i<lst.size(); i++){
        if(i % 2 != 0 && lst[i] % 2 == 0){
            sum += lst[i];
        }
    }
    return sum;
}

int main() {
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}

```

This C++ program defines a function `add` that takes a vector of integers as input and returns the sum of all even elements that are at odd indices in the vector. In the `main` function, we create a vector `lst` and call the `add` function with `lst` as the argument, and then print the result.

The `add` function iterates over the vector using a for loop. For each element, it checks if the index is odd (`i % 2 != 0`) and if the element is even (`lst[i] % 2 == 0`). If both conditions are true, it adds the element to the sum. Finally, the function returns the sum.

In the `main` function, we create a vector `lst` with the elements {4, 2, 6, 7}, call the `add` function with `lst` as the argument, and print the result using `printf`. The output will be `2`, which is the sum of the even elements at odd indices in the vector (2 and 6).