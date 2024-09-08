    string s="";
    s=to_string(x);
    int len=s.length();
    if(shift>len){
        string rev="";
        for(int i=len-1;i>=0;i--){
            rev+=s[i];
        }
        return rev;
    }
    for(int i=len-1;i>=0;i--){
        int j=i+shift;
        if(j<len){
            s[j]=s[i];
        }
        else{
            s[j-len]=s[i];
        }
    }
    return s;

B:
    string s="";
    s=to_string(x);
    int len=s.length();
    if(shift>len){
        string rev="";
        for(int i=len-1;i>=0;i--){
            rev+=s[i];
        }
        return rev;
    }
    for(int i=len-1;i>=0;i--){
        int j=i+shift;
        if(j<len){
            s[j]=s[i];
        }
        else{
            s[j-len]=s[i];
        }
    }
    return s;

C:
    string s="";
    s=to_string(x);
    int len=s.length();
    if(shift>len){
        string rev="";
        for(int i=len-1;i>=0;i--){
            rev+=s[i];
        }
        return rev;
    }
    for(int i=len-1;i>=0;i--){
        int j=i+shift;
        if(j<len){
            s[j]=s[i];
        }
        else{
            s[j-len]=s[i];
        }
    }
    return s;

D:
    string s="";
    s=to_string(x);
    int len=s.length();
    if(shift>len){
        string rev="";
        for(int i=len-1;i>=0;i--){
            rev+=s[i];
        }
        return rev;
    }
    for(int i=len-1;i>=0;i--){
        int j=i+shift;
        if(j<len){
            s[j]=s[i];
        }
        else{
            s[j-len]=s[i];
        }
    }
    return s;

E:
    string s="";
    s=to_string(x);
    int len=s.length();
    if(shift>len){
        string rev="";
        for(int i=len-1;i>=0;i--){
            rev+=s[i];
        }
        return rev;
    }
    for(int i=len-1;i>=0;i--){
        int j=i+shift;
        if(j<len){
            s[j]=s[i];
