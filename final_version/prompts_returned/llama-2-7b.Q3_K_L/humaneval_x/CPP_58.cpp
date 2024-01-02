/*
Return sorted unique common elements for two vectors.
>>> common({1, 4, 3, 34, 653, 2, 5}, {5, 7, 1, 5, 9, 653, 121})
{1, 5, 653}
>>> common({5, 3, 2, 8}, {3, 2})
{2, 3}

*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
	sort(l1.begin(),l1.end());
	sort(l2.begin(),l2.end());
	vector<int> a(60);
	for (int i=0;i<l1.size();++i)
	{
		if (l1[i] == l2[i])
		{
			a.push_back(l1[i]);
		}
	}
	return a;
}
