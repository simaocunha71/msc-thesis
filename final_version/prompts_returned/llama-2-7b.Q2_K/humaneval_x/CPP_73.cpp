/*
Given a vector arr of integers, find the minimum number of elements that
need to be changed to make the vector palindromic. A palindromic vector is a vector that
is read the same backwards and forwards. In one change, you can change one element to any other element.

For example:
smallest_change({1,2,3,5,4,7,9,6}) == 4
smallest_change({1, 2, 3, 4, 3, 2, 2}) == 1
smallest_change({1, 2, 3, 2, 1}) == 0
*/
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
	if(arr.size()==0)return -1;
    int changes=0;
    for(auto i:arr){//for all the elements in array
        if(i%2==0 && (changes == 0 || changes+1 < min(changes, i*i))) {
            return changes + 1;
        }
        changes+=i*(i+1);
    }
    return changes;
}
int main() {
	vector<int> arr={1,2,3,5,4,7,9,6};
	cout<<smallest_change(arr)<<endl;
    vector<int> v{10, 2, 3, 4, 3, 2, 2};
    cout<<smallest_change(v)<<endl;
}
