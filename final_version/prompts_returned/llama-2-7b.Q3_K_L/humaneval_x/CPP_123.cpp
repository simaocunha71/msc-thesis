/*
Given a positive integer n, return a sorted vector that has the odd numbers in collatz sequence.

The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
as follows: start with any positive integer n. Then each term is obtained from the 
previous term as follows: if the previous term is even, the next term is one half of 
the previous term. If the previous term is odd, the next term is 3 times the previous
term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

Note: 
    1. Collatz(1) is {1}.
    2. returned vector sorted in increasing order.

For example:
get_odd_collatz(5) returns {1, 5} // The collatz sequence for 5 is {5, 16, 8, 4, 2, 1}, so the odd numbers are only 1, and 5.
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> result;
    int i = 2, j, sum;
    while (i * i <= n)
        {
            if(n % i == 0 && i%2 != 0)
                {
                    return result;
                }
            i += i;
            
        }
    
    for(j = 1 ; j*j < n ; j++)
    {
        sum = ((int)(n/j)*j + (n%j));
        
        if(sum%2 != 0)
        {
            result.push_back((int)sum);
        }
    }
    
    return result;
}

void main(){
    int n = 7; // test case
    vector<int> result = get_odd_collatz(n);
    for (int i:result) {
        printf("%d\n",i);
    }
    
}