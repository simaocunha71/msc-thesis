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
	for(auto i=l.begin();i!=l.end();i++){ //loop through the list and increment each number by 1
	   *i += 1; 
	}
	return l;
}
int main(){
	vector<int> vec = {3,4,5};//input the vector you wish to increment
	incr_list(vec); //output the list with each number incriment by 1.
	return 0;
}