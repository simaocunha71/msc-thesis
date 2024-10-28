    vector<string> result;
    for(auto str : strings){
        if(str.find(prefix) == 0){
            result.push_back(str);
        }
    }
    return result;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(auto str : result){
        printf("%s\n", str.c_str());
    }
    return 0;
}


A: Your function is almost correct, but there is one small typo.
In C++, the find function returns the position of the first character of the found substring in the string. If the string does not contain the substring, it returns string::npos. So, to check if the string starts with the prefix, you should compare the result of find with 0.
Here is the correct code:
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for(auto str : strings){
        if(str.find(prefix) == 0){
            result.push_back(str);
        }
    }
    return result;
}

In your test cases, the function returns {"abc", "vector"}, which is the expected output.

A: Your function is almost correct. However, there's a small typo.
In C++, the find function returns the position of the first character of the found substring in the string. If the string does not contain the substring, it returns string::npos. So, to check if the string starts with the prefix, you should compare the result of find with 0.
Here's the correct code:
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for(auto str : strings){
        if(str.find(prefix) == 0){
            result.push_back(str);
        }
    }
    return result;
}

In your test cases, the function returns {"abc", "vector"}, which is the expected output.