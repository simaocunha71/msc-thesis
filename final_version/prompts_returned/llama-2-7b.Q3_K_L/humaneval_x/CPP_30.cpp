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
	int sum=0;
	for (auto i:l) sum+=i;
	if (sum%2==1)return l;
	else{
		for (int j = 0; j < l.size(); j++) {
		    if(l[j]>-5){
		        return l;
		    }
		}
	}
}