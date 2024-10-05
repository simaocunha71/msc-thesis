    string result = "";
    int current_base = x;
    while(current_base > 0) {
        result = to_string(current_base % base) + result;
        current_base /= base;
    }
    return result;
}


