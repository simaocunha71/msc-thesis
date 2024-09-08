#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
string get_closest_vowel(string word){
    string vowels = "AEIOUaeiou";
    string result = "";
    for (int i = 0; i < word.length() - 1; i++) {
        if (vowels.find(word[i]) != string::npos && vowels.find(word[i + 1]) != string::npos) {
            result = word[i];
            break;
        }
    }
    return result;
}

B:
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
string get_closest_vowel(string word){
    string vowels = "AEIOUaeiou";
    string result = "";
    for (int i = 0; i < word.length() - 1; i++) {
        if (vowels.find(word[i]) != string::npos && vowels.find(word[i + 1]) != string::npos) {
            result = word[i];
        }
    }
    return result;
}

C:
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
string get_closest_vowel(string word){
    string vowels = "AEIOUaeiou";
    string result = "";
    for (int i = 0; i < word.length() - 1; i++) {
        if (vowels.find(word[i]) != string::npos && vowels.find(word[i + 1]) != string::npos) {
            result = word[i + 1];
        }
    }
    return result;
}

D:
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
string get_closest_vowel(string word){
    string vowels = "AEIOUaeiou";
    string result = "";
    for (int i = 0; i < word.length() - 1; i++) {
        if (vowels.find(word[i]) != string::npos && vowels.find(word[i + 1]) != string::npos) {
            result = word[i + 1];
            break;
        }
    }
    return result;
}

问题要求找到在单词右侧两个辅音之间最近的元音（不区分大小写）。如果找不到这样的元音，应该返回空字符串。

给出的四个选项中，只有选项D满足这个要求。在选项D中，当找到一个元音并且