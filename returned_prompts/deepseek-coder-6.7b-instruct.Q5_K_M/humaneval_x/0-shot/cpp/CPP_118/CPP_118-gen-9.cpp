  string vowels = "AEIOUaeiou";
  for(int i = word.size()-2; i > 0; i--){
    if(vowels.find(word[i]) == string::npos && vowels.find(word[i-1]) != string::npos && vowels.find(word[i+1]) != string::npos){
      return string(1, word[i]);
    }
  }
  return "";
}

int main() {
  printf("%s\n", get_closest_vowel("yogurt").c_str());
  printf("%s\n", get_closest_vowel("FULL").c_str());
  printf("%s\n", get_closest_vowel("quick").c_str());
  printf("%s\n", get_closest_vowel("ab").c_str());
  return 0;
}

The solution provided takes the input string, and iterates over it from right to left (after the first letter). If the current character is not a vowel and the previous and next characters are vowels, it returns the current character. If it doesn't find such a character, it returns an empty string.

I hope this explanation is clear and helpful. If you have any more questions, feel free to ask.
*/
