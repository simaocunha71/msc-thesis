    if (s.length()<3) return false;
    for (int i=0;i<s.length()-2;i++)
    {
        if (s[i]==s[i+1] || s[i]==s[i+2] || s[i+1]==s[i+2])
            return false;
    }
    return true;
}  // This function checks if the string s is happy or not. It first checks if the length of the string is at least 3. If not, it returns false. Then it iterates over the string, checking if any 3 consecutive characters are the same. If it finds any, it returns false. If it doesn't find any, it returns true.  // This function checks if the string s is happy or not. It first checks if the length of the string is at least 3. If not, it returns false. Then it iterates over the string, checking if any 3 consecutive characters are the same. If it finds any, it returns false. If it doesn't find any, it returns true. 
```python
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```


