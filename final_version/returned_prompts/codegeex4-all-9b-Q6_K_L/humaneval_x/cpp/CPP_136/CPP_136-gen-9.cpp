#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst) {
  int max_neg = 0;
  int min_pos = 0;

  for (int i = 0; i < lst.size(); i++) {
    if (lst[i] < 0 && lst[i] < max_neg) {
      max_neg = lst[i];
    }
    if (lst[i] > 0 && lst[i] < min_pos) {
      min_pos = lst[i];
    }
  }

  return {max_neg, min_pos};
}
C:
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst) {
  int max_neg = 0;
  int min_pos = 0;

  for (int i = 0; i < lst.size(); i++) {
    if (lst[i] < 0) {
      if (lst[i] > max_neg) {
        max_neg = lst[i];
      }
    }
    if (lst[i] > 0) {
      if (lst[i] < min_pos) {
        min_pos = lst[i];
      }
    }
  }

  return {max_neg, min_pos};
}
D:
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst) {
  int max_neg = 0;
  int min_pos = 0;

  for (int i = 0; i < lst.size(); i++) {
    if (lst[i] < 0) {
      if (lst[i] > max_neg) {
        max_neg = lst[i];
      }
    }
    if (lst[i] > 0) {
      if (lst[i] < min_pos) {
        min_pos = lst[i];
      }
    }
  }

  return {max_neg, min_pos};
}