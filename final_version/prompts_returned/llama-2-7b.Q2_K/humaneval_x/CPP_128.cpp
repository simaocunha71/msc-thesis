/*
You are given a vector arr of integers and you need to return
sum of magnitudes of integers multiplied by product of all signs
of each number in the vector, represented by 1, -1 or 0.
Note: return -32768 for empty arr.

Example:
>>> prod_signs({1, 2, 2, -4}) == -9
>>> prod_signs({0, 1}) == 0
>>> prod_signs({}) == -32768
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int prod_signs(vector<int> arr){
	if(!arr.size()) return -32768;
	int* pf = new int[arr.size()];
	for (int i=0; i<arr.size(); i++) {p[i]=(arr[i])*(-1);}
	for(int i=0, j=0;i<arr.size();i++){j+=p[i]*pow(2,-j);};
	free(pf);
	return 0;
}
void print_signs(vector<int> arr){
	for (int i=0; i<arr.size(); i++) {printf("%d\n", arr[i]);};
}
int main(){
	vector<int> vec = {1,2,-4}, ans; //create test vector
	print_signs(vec); //print vector contents
	ans=prod_signs(vec), printf("Product of signs of the vector is: %d\n", ans); //Print answer to console
}