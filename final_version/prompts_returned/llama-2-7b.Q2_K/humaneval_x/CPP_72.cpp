/*
Write a function that returns true if the object q will fly, and false otherwise.
The object q will fly if it's balanced (it is a palindromic vector) and the sum of its elements is less than or equal the maximum possible weight w.

Example:
will_it_fly({1, 2}, 5) ➞ false 
// 1+2 is less than the maximum possible weight, but it's unbalanced.

will_it_fly({3, 2, 3}, 1) ➞ false
// it's balanced, but 3+2+3 is more than the maximum possible weight.

will_it_fly({3, 2, 3}, 9) ➞ true
// 3+2+3 is less than the maximum possible weight, and it's balanced.

will_it_fly({3}, 5) ➞ true
// 3 is less than the maximum possible weight, and it's balanced.
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
	if(!q.empty() && (w==0) )//when we have a empty vector or just one element it'll fly without any problem
    {return true;}
	else{for(int i=0;i<q.size();++i)
        {sum=sum+i+q[i];}}
         if((sum==w)&&(sum%2))//when q is an even vector and sum of it's elements are equal with w but not a palindromic vector then yes,it will fly.
             return true;
    else{return false;}
}
int main() {
	vector<int> v={1, 2, 3};//create an empty vector and put the elements from the question in it.
	printf("will_it_fly({1, 2},5) \t\t%s\n", will_it_fly(v, 5)); //in this example i am testing if 1+2 is more than or equals 5 because that's what we are suppose to test it