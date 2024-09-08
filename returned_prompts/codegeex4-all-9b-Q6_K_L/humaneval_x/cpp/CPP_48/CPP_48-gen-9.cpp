#include <iostream>
#include <string>

using namespace std;

bool is_palindrome(string text) {
  int len = text.length();
  for (int i = 0; i < len / 2; i++) {
    if (text[i] != text[len - i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  string text = "aba";
  if (is_palindrome(text)) {
    cout << "true" << endl;
  } else {
    cout << "false" << endl;
  }
  return 0;
}

