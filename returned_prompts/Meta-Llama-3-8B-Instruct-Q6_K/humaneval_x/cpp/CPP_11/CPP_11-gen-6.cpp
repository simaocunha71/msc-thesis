    string res;
    for(int i=0;i<a.length();i++){
        if(a[i] == '1' && b[i] == '1') res += '0';
        else if(a[i] == '0' && b[i] == '0') res += '0';
        else res += '1';
    }
    return res;
}

B:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        if(a[i] == b[i]) res += '0';
        else res += '1';
    }
    return res;
}

C:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        res += to_string(stoi(string(1) + a[i]) ^ stoi(string(1) + b[i]));
    }
    return res;
}

D:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        int x = a[i] - '0', y = b[i] - '0';
        res += (x ^ y) + '0';
    }
    return res;
}

E:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        res += to_string(a[i] ^ b[i]);
    }
    return res;
}

F:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        res += (a[i] - '0') ^ (b[i] - '0') + '0';
    }
    return res;
}

G:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        res += (a[i] ^ b[i]);
    }
    return res;
}

H:
    int res = 0;
    for(int i = 0; i < a.length(); i++){
        res = res ^ (a[i] - '0') ^ (b[i] - '0');
    }
    return to_string(res);
}

I:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        res += (a[i] ^ b[i]);
    }
    return res;
}

J:
    string res = "";
    for(int i = 0; i < a.length(); i++){
        res += (a[i] ^ b[i]);
    }
    return res;
}

K:
   