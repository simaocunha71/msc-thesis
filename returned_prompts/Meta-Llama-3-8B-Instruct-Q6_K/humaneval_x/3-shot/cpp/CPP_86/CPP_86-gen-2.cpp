    string result;
    string temp;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]==' '){
            result+=s[i];
            continue;
        }
        temp=s[i];
        for (int j=i+1;j<s.length();j++)
        {
            if (s[j]<=temp[0]){
                temp=s[j];
                i=j;
            }
        }
        result+=temp;
        i--;
    }
    return result;
} 
```
