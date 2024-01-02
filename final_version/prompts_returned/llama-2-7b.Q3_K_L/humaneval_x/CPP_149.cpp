/*
Write a function that accepts a vector of strings as a parameter,
deletes the strings that have odd lengths from it,
and returns the resulted vector with a sorted order,
The vector is always a vector of strings and never a vector of numbers,
and it may contain duplicates.
The order of the vector should be ascending by length of each word, and you
should return the vector sorted by that rule.
If two words have the same length, sort the vector alphabetically.
The function should return a vector of strings in sorted order.
You may assume that all words will have the same length.
For example:
assert vector_sort({"aa", "a", "aaa"}) => {"aa"}
assert vector_sort({"ab", "a", "aaa", "cd"}) => {"ab", "cd"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> sorted_list_sum(vector<string> lst){
	int max = 0, min = INT_MAX, sum_max=INT_MIN, sum_min = INT_MAX;
   for(int i=0 ; i < (int)lst.size() ; ++i ) {
      int temp = (int)lst[i].size();
      if(temp>sum_max){sum_max=temp;}
      else if(temp<sum_min){sum_min=temp;}
	  max+=temp;
    }
   sort(lst.begin(), lst.end());
//for (int i = 0; i < (int)lst.size(); ++i) {
//   printf(" %d ", lst[i].size());
//}
 //printf("\n");
	return lst;
}
int main()
{
    vector<string> vec = {"aa", "a", "aaa", "abc"};
    cout<<sorted_list_sum(vec)<<endl;
    return 0;
}
