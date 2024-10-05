  string vowels = "aeiouAEIOU";
  for(int i=word.size()-2; i>0; i--){
    if(vowels.find(word[i]) != string::npos && 
       vowels.find(word[i-1]) == string::npos && 
       vowels.find(word[i+1]) == string::npos){
      return string(1,word[i]);
    }
  }
  return "";
}

int main(){
  printf("%s\n", get_closest_vowel("yogurt").c_str());
  printf("%s\n", get_closest_vowel("FULL").c_str());
  printf("%s\n", get_closest_vowel("quick").c_str());
  printf("%s\n", get_closest_vowel("ab").c_str());
}


A: Here is a possible solution using Python:

```python
def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word)-2, 0, -1):
        if (word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels):
            return word[i]
    return ""

print(get_closest_vowel("yogurt"))  # output: "u"
print(get_closest_vowel("FULL"))  # output: "U"
print(get_closest_vowel("quick"))  # output: ""
print(get_closest_vowel("ab"))  # output: ""
```

This function starts from the end of the word and checks if the current character is a vowel and the previous and next characters are not vowels. If it is, it returns the character. If it doesn't find any such character, it returns an empty string.

The time complexity of this function is O(n), where n is the length of the word.

The space complexity is O(1), since no additional space is used that scales with the input