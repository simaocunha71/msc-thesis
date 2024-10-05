  if(strings.empty()){
    return nullptr;
  }
B:
  string longest = strings[0];
  for(auto &s : strings){
    if(s.length() > longest.length()){
      longest = s;
    }
  }
C:
  return longest;
}


int main() {
    vector<string> strings = {"a", "bb", "ccc"};
    printf("%s", longest(strings).c_str());
    return 0;
}


A: Initial check for empty vector.
B: Iterate over the vector of strings, keeping track of longest one found.
C: Return longest string.

The time complexity of this algorithm is O(n), where n is the number of elements in the vector. This is because we are iterating through the vector once to find the longest string.
The space complexity is O(1), as we are only using a constant amount of space to store the longest string and the input vector.
*/


#include<iostream>
#include<vector>
#include<string>
using namespace std;

string longest(vector<string> strings) {
    if(strings.empty()) {
        return nullptr;
    }
    string longest = strings[0];
    for(auto &s : strings){
        if(s.length() > longest.length()){
            longest = s;
        }
    }
    return longest;
}

int main() {
    vector<string> strings = {"a", "bb", "ccc"};
    cout << longest(strings) << endl;
    return 0;
}


































































































































