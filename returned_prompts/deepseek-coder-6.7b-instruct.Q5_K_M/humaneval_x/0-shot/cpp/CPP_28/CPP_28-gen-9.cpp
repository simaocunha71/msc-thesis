    string result = "";
    for(const string& s : strings){
        result += s;
    }
    return result;
}

// Testing
int main(){
    vector<string> test1 = {};
    printf("%s\n", concatenate(test1).c_str());
    vector<string> test2 = {"a", "b", "c"};
    printf("%s\n", concatenate(test2).c_str());
    return 0;
}
```

### 2.

```cpp
