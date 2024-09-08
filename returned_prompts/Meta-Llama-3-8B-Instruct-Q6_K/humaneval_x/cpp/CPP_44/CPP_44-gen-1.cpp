    string result = "";
    while(x > 0){
        int remainder = x % base;
        result = to_string(remainder) + result;
        x = x / base;
    }
    return result;
}

B:
    string result = "";
    while(x > 0){
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
        else
            result = char(remainder + 55) + result;
        x = x / base;
    }
    return result;
}

C:
    string result = "";
    while(x > 0){
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
        else
            result = char(remainder + 55) + result;
        x = x / base;
    }
    return result;
}
D:
    string result = "";
    while(x > 0){
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
        else
            result = char(remainder + 55) + result;
        x = x / base;
    }
    return result;
}

E:
    string result = "";
    while(x > 0){
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
        else
            result = char(remainder + 55) + result;
        x = x / base;
    }
    return result;
}

F:
    string result = "";
    while(x > 0){
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
        else
            result = char(remainder + 55) + result;
        x = x / base;
    }
    return result;
}
G:
    string result = "";
    while(x > 0){
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
        else
            result = char(remainder + 55) + result;
        x = x / base;
    }
    return result;
}

H:
    string result = "";
    while(x > 0){
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
