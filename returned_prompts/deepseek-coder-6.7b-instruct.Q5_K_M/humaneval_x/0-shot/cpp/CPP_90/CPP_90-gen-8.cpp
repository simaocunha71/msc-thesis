    if(lst.size() < 2)
        return NULL;

    sort(lst.begin(), lst.end());

    for(int i = 1; i < lst.size(); i++)
        if(lst[i] > lst[0])
            return lst[i];

    return NULL;
}

int main() {
  vector<int> vect1{1, 2, 3, 4, 5};
  vector<int> vect2{5, 1, 4, 3, 2};
  vector<int> vect3{};
  vector<int> vect4{1, 1};
  
  printf("%d\n", next_smallest(vect1));
  printf("%d\n", next_smallest(vect2));
  printf("%p\n", next_smallest(vect3));
  printf("%p\n", next_smallest(vect4));
  
  return 0;
}
/*
When you run this program, it should print:
2
2
0x0
0x0
*/

*/

//2nd Smallest Number/C++/next_smallest_v2.cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int next_smallest(vector<int> lst){
    if(lst.size() < 2)
        return -1;

    sort(lst.begin(), lst.end());

    for(int i = 1; i < lst.size(); i++)
        if(lst[i] > lst[0])
            return lst[i];

    return -1;
}

int main() {
  vector<int> vect1{1, 2, 3, 4, 5};
  vector<int> vect2{5, 1, 4, 3, 2};
  vector<int> vect3{};
  vector<int> vect4{1, 1};
  
  cout << next_smallest(vect1) << "\n";