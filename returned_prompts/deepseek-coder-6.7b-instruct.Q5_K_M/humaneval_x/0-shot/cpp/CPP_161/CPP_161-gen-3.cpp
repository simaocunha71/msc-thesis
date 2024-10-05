  int len = s.length();
  for(int i = 0; i < len; i++){
    if(isalpha(s[i])){
      if(islower(s[i])){
        s[i] = toupper(s[i]);
      }else{
        s[i] = tolower(s[i]);
      }
    }else{
      for(int j = 0; j < len / 2; j++){
        char temp = s[j];
        s[j] = s[len - 1 - j];
        s[len - 1 - j] = temp;
      }
      return s;
    }
  }
  return s;
}

int main() {
  printf("%s\n", solve("1234").c_str());  // 4321
  printf("%s\n", solve("ab").c_str());  // AB
  printf("%s\n", solve("#a@C").c_str());  // #A@c
  return 0;
}

// #include<stdio.h>
// #include<string>
// using namespace std;

// string solve(string s){
//   for(int i=0;i<s.size();i++)
//     if(isalpha(s[i]))
//       s[i]=islower(s[i])?toupper(s[i]):tolower(s[i]);
//     else
//       reverse(s.begin(),s.end());
//   return s;
// }

// int main() {
//   printf("%s\n", solve("1234").c_str());  // 4321
//   printf("%s\n", solve("ab").c_str());  // AB
//   printf("%s\n", solve("#a@C").c_str());  // #A@c
//   return 0;
// }


// #include<stdio.h>
// #include<string>
// using namespace std;

// string solve(string s){
//   for(char &c:s)
//