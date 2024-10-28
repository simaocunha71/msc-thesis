    vector<string> words;
    string temp = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] == ' ' || s[i] == ','){
            if(temp != ""){
                words.push_back(temp);
                temp = "";
            }
        }
        else{
            temp += s[i];
        }
    }
    if(temp != ""){
        words.push_back(temp);
    }
    return words;
}

int main() {
    vector<string> words = words_string("Hi, my name is John");
    for(int i=0; i<words.size(); i++){
        printf("%s ", words[i].c_str());
    }
    return 0;
}

// 注意，本代码使用了C++标准库，所以需要包含 `<vector>` 和 `<string>` 才能使用 `vector<string>` 和 `string`。
// 函数 `words_string` 接受一个字符串 `s`，并返回一个字符串向量。它遍历字符串 `s`，当遇到空格或逗号时，将当前字符串 `temp` 加入到向量中，并重置 `temp`。最后，如果 `temp` 不为空，将其加入到向量中。
// `main` 函数是用来测试 `words_string` 函数的。它调用 `words_string` 函数，并打印返回的向量。

*/

int main() {
    string s = "Hi, my name is John";
    vector<string> words = words_string(s);
    for(int i=0; i<words.size(); i++){
        cout << words[i] << " ";
    }
    return 0;
}

// 注意，本代码使用了C++标准库，所以需要包含 `<vector>` 和 `<string>` 才能使用 `vector<string>` 和 `string`。
// 函数 `words_string` 接受一个字符