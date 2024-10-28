    vector<int> result;
    for(int i=0;i<n;i++){
        if(n%2==0){
            result.push_back(n+2*i);
        }
        else{
            result.push_back(n+2*i);
        }
    }
    return result;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> result = make_a_pile(n);
    for (int i = 0; i < result.size(); i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
/*
Explanation:
The problem is asking for a program that takes an integer n as an input and returns a vector with the number of stones in each level of a pile. The first level has n stones, and for each subsequent level, the number of stones is either the next odd number if the current level number is odd, or the next even number if the current level number is even.

In the code, we declare a vector result to store the number of stones in each level. Then we use a for loop to iterate from 0 to n-1. In each iteration, we calculate the number of stones in the next level by adding the current level number to 2 times the iteration index. We push this number into the result vector. Finally, we return the result vector.

In the main function, we read the input n, call the make_a_pile function with n as the argument, and then print the result vector.
*/

// S:
/*
Here is the solution in Python:

def make_a_pile(n):
    result = []
    for i in range(n):
        if n%2==0:
            result.append(n+2*i)
        else:
            result.append(n+2*i)
    return result

n = int(input())
result = make_a_pile(n)
for i in range(len(result)):
    print(result[i], end=" ")
*/

// E:
```

```

```
```
```