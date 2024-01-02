/*
Return vector with elements incremented by 1.
>>> incr_vector({1, 2, 3})
{2, 3, 4}
>>> incr_vector({5, 3, 5, 2, 3, 3, 9, 0, 123})
{6, 4, 6, 3, 4, 4, 10, 1, 124}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> incr_list(vector<int> l){
	for(auto i=l.begin();i!=l.end();i++){*i+=1;}
	return l;
}
int main() {
	//Write your code here
	const int SIZE = 5;
	std::vector<int> l{1,2,3};
	std::cout<<"Original list :\n";
	for (auto i:l) std::cout<<i<<' ';
	std::cout << "\n\tIncremented List:\n";
	std::vector<int> ll = incr_list(l);
	for (auto j:ll){
		std::cout<<j<<' ';
	}
	return 0;
}