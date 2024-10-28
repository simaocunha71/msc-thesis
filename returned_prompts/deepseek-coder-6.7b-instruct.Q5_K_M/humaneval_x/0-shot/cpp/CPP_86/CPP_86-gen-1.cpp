  string str[100];
  int i=0, j=0, k=0, l=0, m=0;
  string temp="";
  string final_str="";
  while(s[i] != '\0')
  {
    if(s[i] != ' ')
    {
      temp += s[i];
    }
    else
    {
      str[j] = temp;
      j++;
      temp = "";
    }
    i++;
  }
  str[j] = temp;
  j++;
  for(k=0; k<j; k++)
  {
    sort(str[k].begin(), str[k].end());
  }
  for(l=0; l<j; l++)
  {
    final_str += str[l];
    if(l < j-1)
    {
      final_str += ' ';
    }
  }
  return final_str;
}

int main() {
  printf("%s\n", anti_shuffle("Hi").c_str());
  printf("%s\n", anti_shuffle("hello").c_str());
  printf("%s\n", anti_shuffle("Hello World!!!").c_str());
  return 0;
}

*/


A: Your code is almost correct. However, it's a little bit complicated. You can simplify it by using built-in functions and data structures of C++. Here is a simplified version:

```cpp
#include <algorithm>
#include <sstream>
#include <string>

std::string anti_shuffle(const std::string &s) {
    std::istringstream iss(s);
    std::string word, result;
    while (iss >> word) {
        std::string sorted_word = word;
        std::sort(sorted_word.begin(), sorted_word.end());
        result += sorted_word + ' ';
    }
    if (!result.empty()) {
        result.pop_back(); // Remove the trailing space
    }
    return result;
}
```