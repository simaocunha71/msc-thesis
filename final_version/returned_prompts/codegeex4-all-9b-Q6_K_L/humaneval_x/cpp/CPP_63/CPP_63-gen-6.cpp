The question is asking us to implement a function that computes the n-th element of the FibFib number sequence. The FibFib sequence is defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

To solve this problem, we can use a recursive approach. However, since the FibFib sequence has overlapping subproblems, we can optimize our solution using memoization to avoid redundant calculations.

Here is the implementation of the fibfib function using memoization:

```c++
#include<stdio.h>
#include<map>
using namespace std;

map<int, int> memo;

int fibfib(int n){
    if(n == 0 || n == 1){
        return 0;
    }
    if(n == 2){
        return 1;
    }
    if(memo.find(n) != memo.end()){
        return memo[n];
    }
    memo[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3);
    return memo[n];
}
```

The memo map is used to store the previously computed values of the FibFib sequence. Before computing the value of fibfib(n), we check if it has already been computed and stored in the memo map. If it has, we return the stored value. Otherwise, we compute the value using the recursive definition and store it in the memo map for future use.

This approach has a time complexity of O(n) and a space complexity of O(n) as well, since we need to store the computed values in the memo map.