    vector<string> words;
    string word = "";
    for(auto x : s){
        if(x == ' ' || x == ','){
            if(word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += x;
        }
    }
    if(word != ""){
        words.push_back(word);
    }
    return words;
}
int main(){
    vector<string> v = words_string("Hi, my name is John");
    for(auto x : v){
        printf("%s\n", x.c_str());
    }
    return 0;
}
```

### 题目分析

这道题目要求你写一个函数，将输入的字符串分割成一个单词的向量。单词之间可以通过空格或逗号来分隔。

### 解题思路

这道题目可以通过遍历输入的字符串来解决。当遇到空格或逗号时，将当前的单词添加到结果向量中，并重置单词。在遍历结束后，如果单词不为空，将其添加到结果向量中。

### 代码解析

这段代码首先定义了一个名为words_string的函数，该函数接受一个字符串参数s。然后，它创建了一个空的字符串word和一个空的字符串向量words。

然后，它遍历输入的字符串s。当遇到空格或逗号时，如果当前的单词不为空，它将当前的单词添加到结果向量中，并重置单词。

在遍历结束后，如果当前的单词不为空，它将当前的单词添加到结果向量中。最后，它返回结果向量。

在main函数中，它使用字符串"Hi, my name is John"调用words_string函数，并打印出返回的向量。

### 代码测试

输入："Hi, my name is John"