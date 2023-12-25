/*
You are given a 2 dimensional data, as a nested vectors,
which is similar to matrix, however, unlike matrices,
each row may contain a different number of columns.
Given lst, and integer x, find integers x in the vector,
and return vector of vectors, {{x1, y1}, {x2, y2} ...} such that
each vector is a coordinate - {row, columns}, starting with 0.
Sort coordinates initially by rows in ascending order.
Also, sort coordinates of the row by columns in descending order.

Examples:
get_row({
  {1,2,3,4,5,6},
  {1,2,3,4,1,6},
  {1,2,3,4,5,1}
}, 1) == {{0, 0}, {1, 4}, {1, 0}, {2, 5}, {2, 0}}
get_row({}, 1) == {}
get_row({{}, {1}, {1, 2, 3}}, 3) == {{2, 2}}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<vector<int>> get_row(vector<vector<int>> lst, int x){
	if(x==0||x==lst[0][0]||!lst[0].size()) return vector<vector<int>>(0);
	sort(lst[0].begin(), lst[0].end());
	int n=lst.size();
	vector<vector<int>> ans;
	for(int i=0;i<n;++i){
		if(lst[i][x]!=-1) {ans.emplace_back(vector<int>(x-lst[i][0]));
			for(int j=x-lst[i][0];j<x;++j){
				if(!lst[i+1].empty()) ans[i] = lst[i+1];
				else break;
			}
		}}
	return ans;
}
int main() {return 0;}