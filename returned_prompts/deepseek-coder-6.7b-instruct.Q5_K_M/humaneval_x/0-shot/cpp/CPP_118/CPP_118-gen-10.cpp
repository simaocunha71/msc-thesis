  string vowels="aeiouAEIOU";
  int n=word.size();
  for(int i=n-2;i>0;i--){
    if(vowels.find(word[i])==string::npos && vowels.find(word[i-1])==string::npos && vowels.find(word[i+1])==string::npos){
      return string(1,word[i]);
    }
  }
  return "";
}

int main(){
  printf("%s\n",get_closest_vowel("yogurt").c_str());
  printf("%s\n",get_closest_vowel("FULL").c_str());
  printf("%s\n",get_closest_vowel("quick").c_str());
  printf("%s\n",get_closest_vowel("ab").c_str());
  return 0;
}
*/

S:

The problem is asking to find the closest vowel that stands between two consonants 
from the right side of the word. 

We iterate the word from the right side and check if the current character is a vowel 
and its neighbors are consonants. If it meets the condition, return the current character. 

If we didn't find any such character, return an empty string. 

Time complexity: O(n), where n is the length of the word. We need to scan the whole word from right to left.
Space complexity: O(1), we only use a constant amount of space to store the vowel string and the result.

*/

//end

//source/code/cpp/coding_bat/string-2/get_sandwich.cpp
/*
