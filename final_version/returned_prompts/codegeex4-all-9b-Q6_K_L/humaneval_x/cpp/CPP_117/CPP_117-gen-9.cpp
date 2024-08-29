#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> select_words(string s, int n) {
  vector<string> result;
  string word;
  int consonants = 0;
  for (char c : s) {
    if (isalpha(c)) {
      if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
        consonants++;
      }
      word += c;
    } else {
      if (consonants == n) {
        result.push_back(word);
      }
      consonants = 0;
      word.clear();
    }
  }
  if (consonants == n) {
    result.push_back(word);
  }
  return result;
}

int main() {
  vector<string> words = select_words("Mary had a little lamb", 4);
  for (const string& word : words) {
    cout << word << " ";
  }
  cout << endl;

  return 0;
}
输出：
little
解释：
这段代码实现了题目要求的功能。首先，我们定义了一个函数select_words，它接受一个字符串s和一个整数n作为参数，并返回一个包含所有包含恰好n个辅音字母的单词的向量。

在函数内部，我们使用一个循环遍历字符串s中的每个字符。如果字符是字母，我们检查它是否是辅音字母。如果是辅音字母，我们增加consonants计数器的值，并将字符添加到当前单词word中。如果字符不是字母，我们检查当前单词是否包含恰好n个辅音字母。如果是，我们将当前单词添加到结果向量result中，并将consonants和word重置为0。

最后，我们检查最后一个单词是否包含恰好n个辅音字母。如果是，我们将它添加到结果向量中。最后，我们返回结果向量。

在主函数中，我们使用select_words函数来获取包含恰好4个辅音字母的单词，并将它们打印出来。输出结果为"little"。