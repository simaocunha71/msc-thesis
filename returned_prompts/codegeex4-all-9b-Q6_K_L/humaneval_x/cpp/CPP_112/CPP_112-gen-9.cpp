#include <vector>
#include <string>
using namespace std;

vector<string> reverse_delete(string s, string c) {
  string result = s;
  for (char ch : c) {
    result.erase(remove(result.begin(), result.end(), ch), result.end());
  }
  bool is_palindrome = result == string(result.rbegin(), result.rend());
  return {result, is_palindrome ? "True" : "False"};
}

