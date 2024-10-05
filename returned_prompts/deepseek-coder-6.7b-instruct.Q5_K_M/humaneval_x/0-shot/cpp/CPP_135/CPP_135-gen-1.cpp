  for(int i=arr.size()-1;i>0;i--){
    if(arr[i]<arr[i-1]) return i;
  }
  return -1;
}

*/

// C++ solution
#include<iostream>
#include<vector>
using namespace std;

int can_arrange(vector<int> arr){
  for(int i=arr.size()-1; i>0; i--){
    if(arr[i]<arr[i-1]) return i;
  }
  return -1;
}

int main(){
  vector<int> arr1 = {1,2,4,3,5};
  vector<int> arr2 = {1,2,3};
  cout << can_arrange(arr1) << endl; // should print 3
  cout << can_arrange(arr2) << endl; // should print -1
  return 0;
}

// Time complexity: O(n), where n is the size of the input array
// Space complexity: O(1), since no additional space is used.

// This solution works by iterating over the array in reverse order.
// When it finds an element that is less than the previous one, it returns the index of this element.
// If no such element is found after checking all elements, it returns -1.

// This solution assumes that the input vector will not contain duplicate values.
// If this assumption is not valid, additional checks would need to be added to handle this case.

// This solution assumes that the input vector will always contain at least one element.
// If this assumption is not valid, additional checks would need to be added to handle this case.

// This solution assumes that the input vector will always contain integers.
// If this assumption is not valid, additional checks would need to be added to handle this case.

// This solution assumes that the input vector will always contain positive integers.
// If this assumption is not valid, additional checks would need to be added to handle this case.
// The checks for these assumptions are not included in the solution as they are valid for the given problem.
// However, they should be included in any other similar problems.

// This solution