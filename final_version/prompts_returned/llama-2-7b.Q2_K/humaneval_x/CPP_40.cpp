/*
triples_sum_to_zero takes a vector of integers as an input.
it returns true if there are three distinct elements in the vector that
sum to zero, and false otherwise.

>>> triples_sum_to_zero({1, 3, 5, 0})
false
>>> triples_sum_to_zero({1, 3, -2, 1})
true
>>> triples_sum_to_zero({1, 2, 3, 7})
false
>>> triples_sum_to_zero({2, 4, -5, 3, 9, 7})
true
>>> triples_sum_to_zero({1})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool triples_sum_to_zero(vector<int> l){
	if(l.size() < 3) return false;
	for (auto i: l){
		if(i == 0 || i + l[0] + l[1]){
			return true;
		}
	}
	return false;
}
int main(){
	int i,j;
	vector<int> v={1,2,-3};
	for(i=0;i<=9;++i){
		printf("%d  ",i);
		if((v.size() == 3) && triples_sum_to_zero(v)){
			printf("true\n");
		}else{
			for(j=0;j<9;++j){
				if(triples_sum_to_zero({1,2,-3,i})){
					printf("%d  %d = %d\n",i+1,v[0],v[1]);
				}
			}
		}
	}
	return 0;
}