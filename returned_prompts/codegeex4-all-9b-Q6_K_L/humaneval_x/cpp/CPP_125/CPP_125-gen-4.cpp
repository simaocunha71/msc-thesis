```cpp
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
vector<string> split_words(string txt){
    vector<string> res;
    if(txt.find(' ') != string::npos){
        res = vector<string>(txt.begin(), txt.end());
        remove_if(res.begin(), res.end(), [](string str){ return str == " "; });
    }
    else if(txt.find(',') != string::npos){
        res = vector<string>(txt.begin(), txt.end());
        remove_if(res.begin(), res.end(), [](string str){ return str == ","; });
    }
    else{
        int num = 0;
        for(int i = 0; i < txt.length(); i++){
            if(txt[i] >= 'a' && txt[i] <= 'z'){
                num += txt[i] % 2;
            }
        }
        res.push_back(to_string(num));
    }
    return res;
}
```

I have modified the original code. Now it checks for the existence of spaces and commas in the string. If spaces are found, it splits the string into a vector of words. If commas are found, it splits the string into a vector of words. If neither spaces nor commas are found, it counts the number of lower-case letters with odd order in the alphabet and returns a vector with one element, the number of lower-case letters with odd order in the alphabet.