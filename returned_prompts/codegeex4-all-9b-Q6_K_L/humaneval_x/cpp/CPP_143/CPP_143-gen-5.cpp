/*
You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string should be the same as the original one.

Example 1:
    Input: sentence = "This is a test"
    Output: "is"

Example 2:
    Input: sentence = "lets go for swimming"
    Output: "go for"

Constraints:
    * 1 <= len(sentence) <= 100
    * sentence contains only letters
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

string words_in_sentence(string sentence) {
    string result;
    vector<string> words;
    string word;
    for (char c : sentence) {
        if (c == ' ') {
            if (!word.empty() && is_prime(word.length())) {
                words.push_back(word);
            }
            word.clear();
        } else {
            word += c;
        }
    }
    if (!word.empty() && is_prime(word.length())) {
        words.push_back(word);
    }
    for (const auto& w : words) {
        result += w + " ";
    }
    if (!result.empty()) {
        result.pop_back();
    }
    return result;
}

int main() {
    string sentence;
    cin >> sentence;
    cout << words_in_sentence(sentence) << endl;
    return 0;
}
请问这段代码有什么问题

这段代码的问题在于它没有正确处理输入字符串的最后一个单词。在遍历字符串时，如果最后一个字符不是空格，代码会错误地将最后一个单词添加到`word`变量中，但在添加到`words`向量之前，没有检查该单词的长度是否为质数。此外，如果最后一个单词的长度不是质数，它也不会被添加到结果字符串中。

以下是修复后的代码：

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2