/*
This function takes a vector l and returns a vector l' such that
l' is identical to l in the odd indicies, while its values at the even indicies are equal
to the values of the even indicies of l, but sorted.
>>> sort_even({1, 2, 3})
{1, 2, 3}
>>> sort_even({5, 6, 3, 4})
{3, 6, 5, 4}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<float> sort_even(vector<float> l){
	int odd = 0;
	for (auto val :l) {
		if (floor(val+0.5)>=odd && floor(val-0.5)>=odd)
			++odd;
	}
	sort(l.begin(), l.end());
	return l;
}