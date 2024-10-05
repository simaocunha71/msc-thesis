  if(s.length()<3){
    return false;
  }
  for(int i=0;i<s.length()-2;i++){
    if(s[i]==s[i+1] || s[i]==s[i+2] || s[i+1]==s[i+2]){
      return false;
    }
  }
  return true;
}

int main(){
  printf("%s\n", is_happy("a")? "true" : "false");
  printf("%s\n", is_happy("aa")? "true" : "false");
  printf("%s\n", is_happy("abcd")? "true" : "false");
  printf("%s\n", is_happy("aabb")? "true" : "false");
  printf("%s\n", is_happy("adb")? "true" : "false");
  printf("%s\n", is_happy("xyy")? "true" : "false");
  return 0;
}
```

## Task 2:

Write a program that takes a string and a character as input, and returns a string where all occurrences of the given character in the input string are replaced with underscores.

For example:

replace_char("hello world", 'o') -> "hell_ w_rld"

```cpp
