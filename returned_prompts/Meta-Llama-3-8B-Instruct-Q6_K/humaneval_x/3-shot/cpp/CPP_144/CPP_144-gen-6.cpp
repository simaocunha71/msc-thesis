    float f1 = strtof(x.substr(1).c_str(), NULL);
    float f2 = strtof(n.substr(1).c_str(), NULL);
    float result = f1 / f2;
    return result == (int)result;
}

