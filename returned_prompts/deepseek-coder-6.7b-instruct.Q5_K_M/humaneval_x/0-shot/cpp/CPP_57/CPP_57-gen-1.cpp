  for(int i=0; i<l.size()-1; i++){
    if(l[i]>=l[i+1]){
      return true;
    }
  }
B:
  for(int i=0; i<l.size()-1; i++){
    if(l[i]<=l[i+1]){
      return true;
    }
  }
C:
  return false;
}
*/

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

bool is_monotonic(const vector<int>& v) {
    if (v.size() < 2)
        return true;
    int delta = v[1] - v[0];
    for (size_t i = 2; i < v.size(); ++i) {
        if (delta == 0) {
            delta = v[i] - v[i - 1];
        } else {
            if ((delta > 0 && v[i] - v[i - 1] < 0) || (delta < 0 && v[i] - v[i - 1] > 0)) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    assert(is_monotonic({1, 2, 4, 20}));
    assert(!is_monotonic({1, 20, 4, 10}));
    assert(is_monotonic({4, 1, 0, -10}));
    cout << "All tests passed\n";
    return 0;
}

//C++/lab08/main.cpp
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

bool is_monotonic(const vector<int>& v) {
    if (v.size() < 2)
        return true;
    int delta = v[1] - v[0];
    for (size_t i = 2; i < v.size(); ++i) {
        if (delta == 0)