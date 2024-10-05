  map<int, string> num_to_name = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
  vector<string> res;
  vector<int> temp;

B:
  for(int i = 0; i < arr.size(); i++){
    if(arr[i] >= 1 && arr[i] <= 9){
      temp.push_back(arr[i]);
    }
  }

C:
  sort(temp.begin(), temp.end());
  reverse(temp.begin(), temp.end());

D:
  for(int i = 0; i < temp.size(); i++){
    res.push_back(num_to_name[temp[i]]);
  }
  
E:
  return res;
}
*/

// C++ Solution for the Problem:

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

vector<string> by_length(vector<int> arr){

  map<int, string> num_to_name = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
  vector<string> res;
  vector<int> temp;

  for(int i = 0; i < arr.size(); i++){
    if(arr[i] >= 1 && arr[i] <= 9){
      temp.push_back(arr[i]);
    }
  }

  sort(temp.begin(), temp.end());
  reverse(temp.begin(), temp.end());

  for(int i = 0; i < temp.size(); i++){
    res.push_back(num_to_name[temp[i]]);
  }