/*
Given a vector of non-negative integers, return a copy of the given vector after sorting,
you will sort the given vector in ascending order if the sum( first index value, last index value) is odd,
or sort it in descending order if the sum( first index value, last index value) is even.

Note:
* don't change the given vector.

Examples:
* sort_vector({}) => {}
* sort_vector({5}) => {5}
* sort_vector({2, 4, 3, 0, 1, 5}) => {0, 1, 2, 3, 4, 5}
* sort_vector({2, 4, 3, 0, 1, 5, 6}) => {6, 5, 4, 3, 2, 1, 0}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> array){

    if (array.size()==0)
        return array;
    int first = array[0];
    int last = array.back();
    int sum = first+last;
    if(sum%2==0)
        sort(array.begin(), array.end(), greater<int>());
    else
        sort(array.begin(), array.end());
    return array;
}




int main()
{
    vector<int> nums;
    nums={2, 4, 3, 0, 1, 5};
    vector<int> result = sort_array(nums);
    for(int i=0;i<result.size();i++)
    {
        printf("%d ", result[i]);
    }
    return 0;
}


