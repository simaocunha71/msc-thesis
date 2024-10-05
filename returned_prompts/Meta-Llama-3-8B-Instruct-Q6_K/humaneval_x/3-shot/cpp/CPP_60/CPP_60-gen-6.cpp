    int sum = 0;
    for(int i=1; i<=n; i++)
    {
        sum += i;
    }
    return sum;
} 
// OR 
int sum_to_n(int n){
    return n*(n+1)/2;
} // This is more efficient as it uses formula for sum of sequence from 1 to n. 
// Time complexity is O(1) in this case. 
// In the previous case, time complexity is O(n) as for each number from 1 to n we are doing a constant amount of work. 





