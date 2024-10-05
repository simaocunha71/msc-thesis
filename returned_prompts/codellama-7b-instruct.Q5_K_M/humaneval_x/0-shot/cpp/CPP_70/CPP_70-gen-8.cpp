#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
	vector<int> ans;
	int n = lst.size();
	int min = *min_element(lst.begin(), lst.end());
	int max = *max_element(lst.begin(), lst.end