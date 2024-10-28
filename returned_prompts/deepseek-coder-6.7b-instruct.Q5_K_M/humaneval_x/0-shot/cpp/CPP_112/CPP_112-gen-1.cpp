    for (char ch : c) {
        s.erase(remove(s.begin(), s.end(), ch), s.end());
    }

B:
    string s_rev=s;
    reverse(s_rev.begin(),s_rev.end());

C:
    vector<string> result={s,s==s_rev?"True":"False"};
    return result;
}

int main(){
  string s,c;
  cin>>s>>c;
  vector<string> result=reverse_delete(s,c);
  cout<<result[0]<<" "<<result[1];
  return 0;
}

The code is written in C++. It first removes all the characters from the string s that are present in string c using the STL function remove(). Then it reverses the string s and checks if the resultant string s is same as its reverse. If it is, it returns "True", else "False". The resultant string and the check result are then returned as a vector.
*/

#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
    for (char ch : c) {
        s.erase(remove(s.begin(), s.end(), ch), s.end());
    }
    string s_rev=s;
    reverse(s_rev.begin(),s_rev.end());
    vector<string> result={s,s==s_rev?"True":"False"};
    return result;
}

int main(){
  string s,c;
  cin>>s>>c;
  vector<string> result=reverse_delete(s,c);
  cout<<result[0]<<" "<<result[1];
  return 0;
}

/*
