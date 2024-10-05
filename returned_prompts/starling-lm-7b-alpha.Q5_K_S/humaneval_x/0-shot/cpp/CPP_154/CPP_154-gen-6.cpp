
#include <bits/stdc++.h>
using namespace std;

bool cycpattern_check(string a, string b) {
  // if (b.size() > a.size())
  //   return false;
  if (a.find(b) != string::npos) return true;
  for (int i = 0; i < b.size(); i++) {
    string temp = b.substr(i, b.size());
    if (a.find(temp) != string::npos) return true;
  }
  return false;
}

int main() {
  string a = "himenss";
  string b = "simen";
  if (cycpattern_check(a, b))
    cout << "true" << endl;
  else
    cout << "false" << endl;
}

/*
You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
cycpattern_check("abcd","abd") => false
cycpattern_check("hello","ell") => true
cycpattern_check("whassup","psus") => false
cycpattern_check("abab","baa") => true
cycpattern_check("efef","eeff") => false
cycpattern_check("himenss",'simen") => true

*/

B:
#include <bits/stdc++.h>
using namespace std;

bool cycpattern_check(string a, string b) {
  for (int i = 0; i < b.size(); i++) {
    string temp