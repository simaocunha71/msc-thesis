    vector<string> result;
    vector<string> words;
    string word = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] != ' '){
            word += s[i];
        }else{
            words.push_back(word);
            word = "";
        }
    }
    words.push_back(word);
    for(int i=0; i<words.size(); i++){
        int count = 0;
        for(int j=0; j<words[i].length(); j++){
            if(!isalpha(words[i][j]))
                continue;
            if(!islower(words[i][j]))
                count++;
        }
        if(count == n){
            result.push_back(words[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main()
{
    string s = "Hello world";
    int n = 4;
    vector<string> result = select_words(s,n);
    for(int i=0; i<result.size(); i++)
        printf("%s\n",result[i].c_str());
    return 0;
}
Output:
world
*/

Solution:
The solution to this problem is to split the input string into words, count the number of consonants in each word, and then filter the words that have exactly n consonants. The words are then sorted and returned as a vector.

Here is the C++ code that implements this solution:
```c
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> select_words(string s, int n) {
    vector<string> result;
    vector<string> words;
    string word = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != ' ') {
            word += s[i];
        } else {
            words.push_back(word);
            word = "";
        }
    }
    words.push_back(word);
    for (int i = 0; i < words.size(); i++) {
        int count = 0;
        for (int j = 0; j < words[i].length(); j++) {
            if (!isalpha(words[i][j]))
                continue;
            if (!islower(words[i][j]))
                count++;
        }
        if (count == n) {
            result.push_back(words[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    string s = "