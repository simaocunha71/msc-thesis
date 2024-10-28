  map<int, string> num2words = { {1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"} };
  vector<string> res;
  sort(arr.begin(), arr.end());
  reverse(arr.begin(), arr.end());
  for(int num : arr){
    if(num2words.count(num) > 0){
      res.push_back(num2words[num]);
    }
  }
  return res;
}

int main(){
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> res = by_length(arr);
    for(string s : res){
        printf("%s ", s.c_str());
    }
    return 0;
}

*/

//src/081_090/082_find_the_unique_number.c
#include <stdio.h>

/*
