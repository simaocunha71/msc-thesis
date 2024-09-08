    string res = "";
    while(x > 0){
        int r = x % base;
        res = to_string(r) + res;
        x /= base;
    }
    return res;
}

B:
    string res = "";
    while(x > 0){
        int r = x % base;
        res = (r < 10 ? to_string(r) : string(1, 'A' + r - 10)) + res;
        x /= base;
    }
    return res;
}

C:
    string res = "";
    while(x > 0){
        int r = x % base;
        res = (r < 10 ? to_string(r) : string(1, 'A' + r - 10)) + res;
        x /= base;
    }
    return res;
}
D:
    string res = "";
    while(x > 0){
        int r = x % base;
        if(r < 10)
            res = to_string(r) + res;
        else
            res = (char)(r + 'A' - 10) + res;
        x /= base;
    }
    return res;
}
E:
    string res = "";
    while(x > 0){
        int r = x % base;
        res = (r < 10 ? to_string(r) : string(1, (char)(r + 'A' - 10))) + res;
        x /= base;
    }
    return res;
}

F:
    string res = "";
    while(x > 0){
        int r = x % base;
        res = (char)(r + '0') + res;
        x /= base;
    }
    return res;
}

G:
    string res = "";
    while(x > 0){
        int r = x % base;
        res = (r < 10 ? to_string(r) : string(1, (char)(r + 'A' - 10))) + res;
        x /= base;
    }
    return res;
}

H:
    string res = "";
    while(x > 0){
        int r = x % base;
        res = (char)(r + '0') + res;
        x /= base;
    }
    return res;
}

I:
    string res = "";
    while(x > 0){
        int r = x % base;
        res = (r < 10 ? to_string(r) : string(1,