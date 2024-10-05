/*
Write a recursive function, f(x), that takes in a string x and returns the number of characters in x.
*/
#include <string>
using namespace std;
int f(string x) {
  if (x.length() == 0) {
    return 0;
  } else {
    return 1 + f(x.substr(1));
  }
}

