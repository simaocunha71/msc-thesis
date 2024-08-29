```cpp
vector<string> all_prefixes(string str){
    vector<string> result;
    for(int i=0;i<str.length();i++){
        result.push_back(str.substr(i));
    }
    return result;
}
```
这个代码段从位置`i`开始获取整个字符串的子串。所以对于字符串"abc"，输出将是：
```
{"abc", "bc", "c"}
```

B:
```cpp
vector<string> all_prefixes(string str){
    vector<string> result;
    for(int i=0;i<str.length();i++){
       