    vector<string> result;
    for(int i=0; i<strings.size(); i++){
        if(strings[i].find(substring) != string::npos){
            result.push_back(strings[i]);
        }
    }
    return result;
}

int main(){
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for(int i=0; i<result.size(); i++){
        printf("%s\n", result[i].c_str());
    }
    return 0;
}
```

This code will work for C++. It takes a vector of strings and a substring as inputs, then it iterates over the strings vector and checks if the current string contains the provided substring. If it does, it adds the string to the result vector. Finally, it returns the result vector.

In the main function, we use this function to filter a vector of strings that contain the substring "a", and print the result.

