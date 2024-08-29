#include <iostream>
#include <string>

using namespace std;

bool is_nested(string str) {
  int open_brackets = 0;
  int max_open_brackets = 0;

  for (char c : str) {
    if (c == '[') {
      open_brackets++;
      max_open_brackets = max(max_open_brackets, open_brackets);
    } else if (c == ']') {
      open_brackets--;
    }
  }

  return max_open_brackets > 1;
}

int main() {
  cout << is_nested("[[]]") << endl;  // 1
  cout << is_nested("[]]]]]]][[[[[]") << endl;  // 0
  cout << is_nested("[][]") << endl;  // 0
  cout << is_nested("[]") << endl;  // 0
  cout << is_nested("[[][]]") << endl;  // 1
  cout << is_nested("[[]][[") << endl;  // 1
  return 0;
}