    vector<string> result;
    string temp = s;
    for(int i=0;i<c.length();i++){
        temp.erase(remove(temp.begin(),temp.end(),c[i]),temp.end());
    }
    result.push_back(temp);
    if(is_palindrome(temp)){
        result.push_back("True");
    }else{
        result.push_back("False");
    }
    return result;
}

bool is_palindrome(string s){
    int start = 0;
    int end = s.length()-1;
    while(start<=end){
        if(s[start]!=s[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main(){
    string s = "abcdedcba";
    string c = "ab";
    vector<string> result = reverse_delete(s,c);
    for(auto i:result){
        cout<<i<<endl;
    }
    return 0;
}
Solutions:

1.  The function `reverse_delete` takes two strings `s` and `c` as input. It first creates a temporary copy of the string `s`. Then it iterates over each character in the string `c` and removes all occurrences of that character from the temporary copy of `s` using the `erase` and `remove` functions. The resulting string is then added to the result vector.

The function then checks if the resulting string is a palindrome by calling the `is_palindrome` function. If the string is a palindrome, the function adds the string "True" to the result vector, otherwise it adds the string "False".

The `is_palindrome` function takes a string as input and checks if it is a palindrome by comparing characters from the start and end of the string and moving towards the center. If it finds any pair of characters that are not equal, it returns `false`, otherwise it returns `true`.

In the `main` function, we call the `reverse_delete` function with the strings "abcdedcba" and "ab" as input, and print the result.

Output:

```
cdedc
True
```

2.  The function `reverse_delete` takes two strings `s` and `c` as input. It first creates a temporary copy of the string `s`. Then it iterates over each character in the string `c` and removes all occurrences of that character from the temporary copy of `s` using the `erase` and `remove` functions. The resulting string is then added to the result vector