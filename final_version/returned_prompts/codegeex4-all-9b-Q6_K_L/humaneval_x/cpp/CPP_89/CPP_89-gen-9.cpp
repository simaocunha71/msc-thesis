#include <iostream>
#include <string>

using namespace std;

string encrypt(string s){
  string result = "";
  for(int i = 0; i < s.length(); i++){
    if(s[i] == 'z' || s[i] == 'Z'){
      result += 'a';
    }
    else if(s[i] == 'y' || s[i] == 'Y'){
      result += 'b';
    }
    else if(s[i] == 'x' || s[i] == 'X'){
      result += 'c';
    }
    else{
      result += s[i] + 4;
    }
  }
  return result;
}

int main() {
  string str;
  getline(cin, str);

  cout << encrypt(str) << endl;

  return 0;
}

B:
#include <iostream>
#include <string>

using namespace std;

string encrypt(string s){
  string result = "";
  for(int i = 0; i < s.length(); i++){
    if(s[i] == 'z' || s[i] == 'Z'){
      result += 'a';
    }
    else if(s[i] == 'y' || s[i] == 'Y'){
      result += 'b';
    }
    else if(s[i] == 'x' || s[i] == 'X'){
      result += 'c';
    }
    else{
      result += s[i] + 4;
    }
  }
  return result;
}

int main() {
  string str;
  getline(cin, str);

  cout << encrypt(str) << endl;

  return 0;
}

C:
#include <iostream>
#include <string>

using namespace std;

string encrypt(string s){
  string result = "";
  for(int i = 0; i < s.length(); i++){
    if(s[i] == 'z' || s[i] == 'Z'){
      result += 'a';
    }
    else if(s[i] == 'y' || s[i] == 'Y'){
      result += 'b';
    }
    else if(s[i] == 'x' || s[i] == 'X'){
      result += 'c';
    }
    else{
      result += s[i] + 4;
    }
  }
  return result;
}

int main() {
  string str;
  getline(cin, str);

  cout << encrypt(str) << endl;

  return 0;
}

D:
#include <iostream>
#include <string>

using namespace std