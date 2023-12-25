/*
This function takes a vector l and returns a vector l' such that
l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
to the values of the corresponding indicies of l, but sorted.
>>> sort_third({1, 2, 3})
{1, 2, 3}
>>> sort_third({5, 6, 3, 4, 8, 9, 2})
{2, 6, 3, 4, 8, 9, 5}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_third(vector<int> l){
	vector<int> l_prime = l;
	//sort from largest to smallest
	for ( int i=0; i<l.size(); i++ ){
		if ( l[i] % 3 != 0 )
			l_prime[i]=max(l_prime[i],1);
	}
	//sort from smallest to largest
	for ( int i=0; i<l.size(); i++ ){
		if ( l[i] % 3 != 0 )
			l_prime[i]=min(l_prime[i],1);
	}
	return l_prime;
}