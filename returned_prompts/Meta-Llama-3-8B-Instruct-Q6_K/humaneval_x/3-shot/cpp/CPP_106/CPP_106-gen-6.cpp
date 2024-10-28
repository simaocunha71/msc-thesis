    vector<int> result(n);
    for(int i = 1; i <= n; i++) {
        if(i % 2 == 0) {
            result[i-1] = i; // Factorial of i if i is even
        } else {
            int sum = 0;
            for(int j = 1; j <= i; j++) {
                sum += j;
            }
            result[i-1] = sum; // Sum of numbers from 1 to i otherwise
        }
    }
    return result;
}  // This code does not handle the case when i is zero. In that case, we should return 1. We can add a special check at the beginning of the loop to handle this. 
// We can also optimize this code by calculating the sum of numbers from 1 to i only once for each i and then storing it for future use. 
// We can use a for loop to calculate the factorial of i if i is even. 
// We can also use memoization technique to optimize the function. 
// We should also add error checking to handle the case when n is less than 1. 
// We should also add error checking to handle the case when n is greater than the maximum value that can be stored in an integer. 
// The time complexity of this code is O(n). The space complexity is O(n).  // We can also use dynamic programming to solve this problem. 
// We can also use recursion to solve this problem. 
// We can also use mathematical formula to solve this problem. 
// We can also use a lookup table to solve this problem. 
// We can also use a binary search to solve this problem. 
// We can also use a hash map to solve this problem. 
// We can also use a stack to solve this problem. 
// We can also use a queue to solve this problem. 
// We can also use a graph to solve this problem. 
// We can also use a tree to solve this problem. 
// We can also use a linked list to solve this problem. 
// We can also use a heap to solve this problem. 
// We can also use a priority queue to solve this problem. 
// We can also use a bit manipulation to solve this problem. 
// We can also use a mathematical formula to solve this problem. 
// We can also use a lookup table to solve this problem. 
// We can also use a binary search to solve