
}
*/

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_vector(vector<int> array){

  vector<int> arr = array;
  int sum = arr[0] + arr[arr.size() - 1];
  if(sum % 2 == 0)
    sort(arr.begin(), arr.end(), greater<int>());
  else
    sort(arr.begin(), arr.end());
  return arr;
}

int main() {
  vector<int> arr = {2, 4, 3, 0, 1, 5, 6};
  vector<int> sorted_arr = sort_vector(arr);
  for(int i = 0; i < sorted_arr.size(); i++)
    printf("%d ", sorted_arr[i]);
  return 0;
}
```

This code defines a function named `sort_vector` that accepts a vector of integers and returns a sorted copy of the vector. The sorted order is determined by whether the sum of the first and last elements of the vector is odd or even. If the sum is odd, the vector is sorted in ascending order; if the sum is even, the vector is sorted in descending order.

The code includes the necessary headers for the `vector` and `algorithm` libraries, defines the `sort_vector` function, and includes a `main` function for testing the `sort_vector` function. The `main` function creates a vector of integers, calls `sort_vector` to get a sorted copy of the vector, and then prints the elements of the sorted vector.

The `sort` function from the `algorithm` library is used to sort the vector. The `greater<int>()` function object is passed as the third argument to `sort` to sort the vector in descending order. If the sum of the first and last elements is odd, the vector is sorted in ascending order by default.

Note: This code assumes that the input vector will always have at least one element.

I hope this helps you understand how to solve the problem.
*/





















