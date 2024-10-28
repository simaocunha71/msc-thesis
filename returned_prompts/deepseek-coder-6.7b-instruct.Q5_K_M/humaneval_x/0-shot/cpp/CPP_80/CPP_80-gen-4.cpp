    if(s.size() < 3){
        return false;
    }
    for(int i = 0; i < s.size() - 2; i++){
        if(s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2]){
            return false;
        }
    }
    return true;
}
int main(){
    string s;
    cin>>s;
    if(is_happy(s)){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
}
```

**Explanation:**

The program checks if the size of the string is less than 3. If yes, it returns false. 

If not, it iterates through the string checking if the characters at position i, i+1, and i+2 are the same (i.e., if any two of them are the same or all three are the same). If it finds any such case, it returns false.

If it doesn't find any such case, it returns true, indicating that the string is happy.

This solution has a time complexity of O(n), where n is the length of the string.

























































































































































































































