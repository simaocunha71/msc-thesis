  string alphabet="abcdefghijklmnopqrstuvwxyz";
  string ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  string result="";
  for(int i=0;i<s.size();i++){
    if(alphabet.find(s[i]) != string::npos){
      result += ALPHABET[alphabet.find(s[i])];
    }
    else if(ALPHABET.find(s[i]) != string::npos){
      result += alphabet[ALPHABET.find(s[i])];
    }
    else{
      result = s[i] + result;
    }
  }
  return result;
}

int main(){
  printf("%s\n",solve("1234").c_str());
  printf("%s\n",solve("ab").c_str());
  printf("%s\n",solve("#a@C").c_str());
  return 0;
}
```

## Task 2

```cpp
