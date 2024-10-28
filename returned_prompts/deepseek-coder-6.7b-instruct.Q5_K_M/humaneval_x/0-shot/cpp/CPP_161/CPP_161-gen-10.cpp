  int i;
  int len=s.length();
  for(i=0;i<len;i++){
    if(isalpha(s[i])){
      if(islower(s[i])){
        s[i]=toupper(s[i]);
      }
      else{
        s[i]=tolower(s[i]);
      }
    }
  }
  if(isalpha(s[0])){
    return s;
  }
  else{
    reverse(s.begin(), s.end());
    return s;
  }
}

int main()
{
    // Testcase 1
    string s = "1234";
    printf("%s\n", solve(s).c_str());

    // Testcase 2
    s = "ab";
    printf("%s\n", solve(s).c_str());

    // Testcase 3
    s = "#a@C";
    printf("%s\n", solve(s).c_str());

    return 0;
}
```

## 2. Python code

```python
def solve(s):
    if all(not c.isalpha() for c in s):
        return s[::-1]
    return ''.join(c.upper() if c.islower() else c.lower() for c in s)

# Testcase 1
s = "1234"
print(solve(s))

# Testcase 2
s = "ab"
print(solve(s))

# Testcase 3
s = "#a@C"
print(solve(s))
```

## 3. JavaScript code

```javascript
function solve(s) {
    let isLetter = /[a-z]/i;
    let isUpperCase = /[A-Z]/;
    let result = "";
    for (let i = 0; i < s.length; i++) {
        if (!isLetter.test(s[i])) {
            result += s[i];
        } else {
            if (isUpper