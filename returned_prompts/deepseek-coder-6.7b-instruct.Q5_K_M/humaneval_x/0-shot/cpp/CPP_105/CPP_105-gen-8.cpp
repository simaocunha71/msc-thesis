  vector<string> names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
  map<int, string> m;
  for(int i=0; i<names.size(); i++) m[i+1] = names[i];
  vector<int> valid;
  for(int i=0; i<arr.size(); i++) if(arr[i]>=1 && arr[i]<=9) valid.push_back(arr[i]);
  sort(valid.begin(), valid.end());
  reverse(valid.begin(), valid.end());
  vector<string> res;
  for(int i=0; i<valid.size(); i++) res.push_back(m[valid[i]]);
  return res;
}

*/

#include<stdio.h>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

vector<string> by_length(vector<int> arr) {
  vector<string> names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
  map<int, string> m;
  for(int i=0; i<names.size(); i++) m[i+1] = names[i];
  
  vector<int> valid;
  for(int i=0; i<arr.size(); i++) if(arr[i]>=1 && arr[i]<=9) valid.push_back(arr[i]);
  
  sort(valid.begin(), valid.end());
  reverse(valid.begin(), valid.end());
  
  vector<string> res;
  for(int i=0; i<valid.size(); i++) res.push_back(m[valid[i]]);
  return res;
}

int main(){
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string