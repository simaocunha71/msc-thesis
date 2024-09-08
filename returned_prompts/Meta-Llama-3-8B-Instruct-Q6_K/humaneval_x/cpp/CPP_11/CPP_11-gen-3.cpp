    int len = a.length();
    string result;
    for(int i=0; i<len; i++){
        if(a[i] == '1' && b[i] == '1')
            result += '0';
        else if(a[i] == '0' && b[i] == '0')
            result += '0';
        else
            result += '1';
    }
    return result;
}

B:
    string result;
    for(int i=0; i<a.length(); i++){
        if(a[i] == b[i])
            result += '0';
        else
            result += '1';
    }
    return result;

C:
    int len = a.length();
    string result;
    for(int i=0; i<len; i++){
        if(a[i] != b[i])
            result += '1';
        else
            result += '0';
    }
    return result;

D:
    int len = a.length();
    string result;
    for(int i=0; i<len; i++){
        if(a[i] == '1')
            result += '1';
        else
            result += '1';
    }
    return result;

E:
    int len = a.length();
    string result;
    for(int i=0; i<len; i++){
        if(a[i] == '0')
            result += '1';
        else
            result += '0';
    }
    return result;

F:
    int len = a.length();
    string result;
    for(int i=0; i<len; i++){
        if(a[i] == '1' && b[i] == '0')
            result += '1';
        else
            result += '0';
    }
    return result;

G:
    int len = a.length();
    string result;
    for(int i=0; i<len; i++){
        if(a[i] == '0' && b[i] == '1')
            result += '1';
        else
            result += '0';
    }
    return result;

H:
    int len = a.length();
    string result;
    for(int i=0; i<len; i++){
        if(a[i] == '1' && b[i] == '1')
            result += '0';
        else
            result += '1';
    }
    return result;

I:
    int len = a.length();
    string result;
    for(int i=0; i<len;