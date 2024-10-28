    if (n<=1)
    return n;
    else
    return fib(n-1)+fib(n-2);
}
//This code is incorrect, it will cause a stack overflow for n>12.
//A better solution would be to use a loop and keep track of the last two numbers in the sequence. 
//This is known as memoization. 
int fib(int n){
    if (n<=1)
    return n;
    int prev2=0;
    int prev=1;
    for (int i=2;i<=n;i++){
        int curr=prev+prev2;
        prev2=prev;
        prev=curr;
    }
    return prev;
} 
//This solution has a time complexity of O(n) and a space complexity of O(1), much better than the original recursive solution. 
//However, it still has to store all the intermediate results in memory, which might be a problem for very large values of n. 
//A more space-efficient solution would be to use a single variable to keep track of the last number in the sequence. 
int fib(int n){
    if (n<=1)
    return n;
    int prev=0;
    int curr=1;
    for (int i=2;i<=n;i++){
        int newcurr=prev+curr;
        prev=curr;
        curr=newcurr;
    }
    return curr;
} 
//This solution has a time complexity of O(n) and a space complexity of O(1), and it only needs to store the last two numbers in the sequence. 
//This is the best solution you can get for this problem. 
//It is also known as the "online algorithm" because it does not need to store all the intermediate results in memory. 
//It is the most efficient solution for this problem. 







