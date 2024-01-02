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
	if(l.size()==0) return false;
	if (l.size()==1) {
	  if (l[0] ==0 )
        return true; //return true if the vector has a triplet of zeroes
    } else if (l[0]+l[1] == 0 && l[1]+l[2] == 0 && l[2]+l[3] == 0) {
        return true;
    }
	return false;
}
int main(){
//testing triples_sum_to_zero
int a[]={4,6,-5};
printf("a=%d",a);
if(triples_sum_to_zero(a)){
  printf("sum to zero");
}else{
  printf("not sum to zero");
}
return 0;
}
