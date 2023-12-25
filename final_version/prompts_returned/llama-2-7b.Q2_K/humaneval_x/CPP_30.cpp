/*
Return only positive numbers in the vector.
>>> get_positive({-1, 2, -4, 5, 6})
{2, 5, 6}
>>> get_positive({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
{5, 3, 2, 3, 9, 123, 1}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
	int index = 0;
	for (index = 0, index = 0; index < length(l); index++)
		if (l[index] >= 0)
			break;
	return l.begin() + index;
}

