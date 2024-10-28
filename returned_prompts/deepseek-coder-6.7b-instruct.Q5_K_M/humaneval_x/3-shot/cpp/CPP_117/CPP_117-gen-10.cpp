/*
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pipix") → "3.14x"
*/
#include <string>
using namespace std;
string changePi(string str) {
  if (str.size() < 2) return str;
  if (str.substr(0, 2) == "pi")
    return "3.14" + changePi(str.substr(2));
  else
    return str[0] + changePi(str.substr(1));
}


