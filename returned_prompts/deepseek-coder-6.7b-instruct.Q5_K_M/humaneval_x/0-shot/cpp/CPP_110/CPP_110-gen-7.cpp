
}
int main(){
  vector<int> lst1{1, 2, 3, 4}, lst2{1, 2, 3, 4};
  printf("%s", exchange(lst1, lst2).c_str());
  return 0;
}
*/

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1, vector<int> lst2){
  int odd1 = 0, odd2 = 0;
  for(int i = 0; i < lst1.size(); i++)
    if(lst1[i] % 2) odd1++;
  for(int i = 0; i < lst2.size(); i++)
    if(lst2[i] % 2 == 0) odd2++;
  return (odd1 <= odd2) ? "YES" : "NO";
}
int main(){
  vector<int> lst1{1, 2, 3, 4}, lst2{1, 2, 3, 4};
  printf("%s", exchange(lst1, lst2).c_str());
  return 0;
}

// Test Cases:
// exchange({1, 2, 3, 4}, {1, 2, 3, 4}) -> "YES"
// exchange({1, 2, 3, 4}, {1, 5, 3, 4}) -> "NO"
// exchange({2, 2, 2, 2}, {1, 3, 3, 3}) -> "YES"
// exchange({1, 3, 5, 7}, {2, 4, 6, 8}) -> "YES"
// exchange({2, 4, 6, 8}, {1, 3, 5, 7}) -> "YES"
// exchange({1, 1, 1, 1}, {2, 2, 2, 2}) -> "YES"
// exchange({2, 2,