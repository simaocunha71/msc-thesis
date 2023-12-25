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
	vector<int> v;
	if(l1[0]=='9'){
		v=l1;
	}else{
		if(l1.size()==l2.size()){
			for(int i=0;i<l1.size();++i)if(!v.count((*l1)[i])) v.push_back((*l1)[i]);
		}else{
			v=l1;
		}
	}
	return v;
}
int main()
{
	vector<int> l1={'9','5','4','3'};
	vector<int> l2={'5','7','1','5','9','653','121'};
	printf("%d\n",common(l1,l2).size());
}
