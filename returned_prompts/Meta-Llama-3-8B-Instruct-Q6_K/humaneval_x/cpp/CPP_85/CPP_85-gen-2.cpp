    int sum = 0;
    for(int i = 1; i < lst.size(); i+=2){
        if(lst[i]%2==0){
            sum += lst[i];
        }
    }
    return sum;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}

```

The code provided is a simple implementation of the problem in C++. It defines a function `add` that takes a vector of integers `lst` as input and returns the sum of even elements at odd indices.

Here's a step-by-step breakdown of the code:

1. The function `add` is defined, which takes a vector of integers `lst` as input.
2. An integer `sum` is initialized to 0, which will be used to store the sum of even elements at odd indices.
3. A `for` loop is used to iterate through the elements of the vector, starting from the second element (index 1) and incrementing the index by 2 in each iteration.
4. Inside the loop, the condition `lst[i]%2==0` checks if the current element is even. If it is, the element is added to the `sum`.
5. The function returns the `sum` value.

In the `main` function, a vector `lst` is created with the elements {4, 2, 6, 7}. The `add` function is called with `lst` as input, and the result is printed to the console.

When you run this code, it will output `2`, which is the sum of even elements at odd indices in the input vector.