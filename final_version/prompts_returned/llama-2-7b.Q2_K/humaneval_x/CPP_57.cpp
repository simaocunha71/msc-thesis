/*
Return true is vector elements are monotonically increasing or decreasing.
>>> monotonic({1, 2, 4, 20})
true
>>> monotonic({1, 20, 4, 10})
false
>>> monotonic({4, 1, 0, -10})
true
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
	if(l[0] < l[1]){
	    return (l[0] < l[2] && l[1] > -INFINITY);
   }else if(l[0] > l[1]){
      return (l[0] > -INFINITY && l[2] > -INFINITY); 
   }else
    return true;
}
int main(){
	vector<float> a = {1.5f, 2.3f, 24f};
	if(monotonic(a))printf("true\n");
	else printf("false\n");
   vector<float> b = {-10,-INFINITY};
   if(monotonic(b))printf("true\n");
   else printf("false\n");
}
