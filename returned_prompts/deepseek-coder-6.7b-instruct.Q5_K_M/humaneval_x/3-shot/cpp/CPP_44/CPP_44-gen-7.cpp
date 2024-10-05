    string result;
    while (x) {
        result = to_string(x % base) + result;
        x /= base;
    }
    return result;
}

