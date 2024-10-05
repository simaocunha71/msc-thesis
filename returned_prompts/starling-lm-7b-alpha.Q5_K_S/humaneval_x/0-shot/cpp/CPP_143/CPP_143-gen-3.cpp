
#include<bits/stdc++.h>
using namespace std;

vector<string> split(const string &s, char delim) {
  stringstream ss(s);
  string item;
  vector<string> tokens;
  while (getline(ss, item, delim)) {
    tokens.push_back(item);
  }
  return tokens;
}

string words_in_sentence(string sentence)
{
    vector<string> v=split(sentence,' ');
    string ret;
    for(int i=0;i<v.size();i++)
    {
        if(isPrime(v[i].size())) ret+=v[i]+" ";
    }
    return ret;
}

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;

    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (