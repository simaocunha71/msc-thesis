
#include <stdio.h>
#include <vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst) {

  int a = 0, b = 0;

  for (int i = 0; i < lst.size(); i++) {
    if (lst[i] < 0 && lst[i] > a) {
      a = lst[i];
    }
    if (lst[i] > 0 && lst[i] < b) {
      b = lst[i];
    }
  }

  vector<int> integers;
  integers.push_back(a);
  integers.push_back(b);

  return integers;
}
*/
