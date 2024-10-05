	sort(l.begin(), l.end());
	
B:
	vector<int> res;
	res.clear();
	res.push_back(l[0]);
	for(int i = 1; i < l.size(); ++i){
		if(l[i] != l[i - 1]){
			res.push_back(l[i]);
		}
	}

C:
	return res;


*/

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> unique(