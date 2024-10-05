  int len=word.length();
  for(int i=len-2;i>0;i--){
    if(isalpha(word[i-1]) && isalpha(word[i+1])){
      if(word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'||
      word[i]=='A'||word[i]=='E'||word[i]=='I'||word[i]=='O'||word[i]=='U')
      return string(1,word[i]);
    }
  }
  return "";
}
*/


#include <stdio.h>
#include <ctype.h>
#include <string.h>

char get_closest_vowel(char *word){

  int len=strlen(word);
  for(int i=len-2;i>0;i--){
    if(isalpha(word[i-1]) && isalpha(word[i+1])){
      if(word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'||
      word[i]=='A'||word[i]=='E'||word[i]=='I'||word[i]=='O'||word[i]=='U')
      return word[i];
    }
  }
  return '\0';
}

int main(){
  printf("%c\n", get_closest_vowel("yogurt"));
  printf("%c\n", get_closest_vowel("FULL"));
  printf("%c\n", get_closest_vowel("quick"));
  printf("%c\n", get_closest_vowel("ab"));
  return 0;
}
```

In this program, we define a function named get_closest_vowel which takes a string as input and returns the closest vowel to the right side