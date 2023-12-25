/*
Given a positive integer n, you have to make a pile of n levels of stones.
The first level has n stones.
The number of stones in the next level is:
    - the next odd number if n is odd.
    - the next even number if n is even.
Return the number of stones in each level in a vector, where element at index
i represents the number of stones in the level (i+1).

Examples:
>>> make_a_pile(3)
{3, 5, 7}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> make_a_pile(int n){
	if(!n%2)
		return {1,4};// n is odd
	else if(!n%3)// n is divisible by 3 (so n is even)
		return {1,2,6};
}
int main()
{
	vector<int> answer = make_a_pile(7);
	printf("%d\n",answer[0]);
	for(int i=1;i<7+1;++i)
		printf("%d ",answer[i]);
}
/*
I tried to solve it by brute force:
int next_even = 3, n, next_odd = 5, next_even;
for(n=0;n<=6;++n){
    if(!next_even && !next_od)return;// if no more even or odd numbers to try
	if((!(next_even&1))&&(next_even%2!=0)){next_odd+=1;}else{next_even+=1}}
*/
/*
There is a way: n/4-3n/8+9 can be used.
There are 3 cases to handle.
The first case is n divisible by four, then we get a remainder of 0 or positive number (that is always even).
It means that the next odd number will do here.
If n is not divisible by four, we have to find an even number in the range [1;n-2] and add the number.
The second case is when n is exactly divisible by 4