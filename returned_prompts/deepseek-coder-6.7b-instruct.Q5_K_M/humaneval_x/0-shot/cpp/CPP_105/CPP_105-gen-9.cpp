  map<int, string> num_names = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
  vector<string> res;
  sort(arr.begin(), arr.end());
  reverse(arr.begin(), arr.end());
  for(int i = 0; i < arr.size(); i++){
    if(arr[i] >= 1 && arr[i] <= 9){
      res.push_back(num_names[arr[i]]);
    }
  }
  return res;
}

int main(){
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> res = by_length(arr);
  for(int i = 0; i < res.size(); i++){
    printf("%s ", res[i].c_str());
  }
  return 0;
}

*/

/*
The code reads a list of integers from the input vector, sorts them in ascending order, then reverses the order. After that, it maps each integer from 1 to 9 to its corresponding string name from "One" to "Nine" in a map and pushes the corresponding string names into the result vector. If the integer is not in the range of 1 to 9, it is ignored.
*/


/*
The time complexity of this algorithm is O(n log n) due to the sorting step. The space complexity is O(n) since we are storing the result in a new vector.
*/

/*
This problem can be solved in a more efficient way by using a frequency count approach. The frequency of each number from 1 to 9 can be counted and then the numbers are appended to the result vector in decreasing order of frequency. This approach will be more efficient for larger input vectors and will reduce the time complexity to O(n).
*/

/*
The frequency count approach can be implemented in C++ as follows:

```cpp
#include<vector>
#include<string