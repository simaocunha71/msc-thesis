The provided solution is incorrect. Here is the correct solution:

```cpp
#include<vector>
int solution(vector<int> lst){
    int res = 0;
    for(int i=0;i<lst.size();i++){
        if(i%2 == 0 && lst[i]%2 != 0){
            res += lst[i];
        }
    }
    return res;
}

int main(){
    vector<int> lst = {5, 8, 7, 1};
    printf("%d\n",solution(lst));
    return 0;
}
```

Explanation:
The provided solution is incorrect because the condition in the if statement is incorrect. It should be `i%2 == 0` instead of `i%2 != 0`. This is because we want to find the odd elements in even positions, not the even elements in even positions.

The correct solution is as follows:

1. Define a function `solution` that takes a vector of integers as input and returns an integer.
2. Initialize a variable `res` to 0 to store the sum of odd elements in even positions.
3. Use a for loop to iterate through the elements of the vector.
4. Inside the loop, check if the index `i` is even (i%2 == 0) and the value at index `i` is odd (lst[i]%2 != 0). If both conditions are true, add the value at index `i` to `res`.
5. After the loop, return the value of `res`.
6. In the `main` function, create a vector `lst` with some sample values.
7. Call the `solution` function