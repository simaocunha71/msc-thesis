    string str_a=boost::any_cast<string>(a);
    string str_b=boost::any_cast<string>(b);
    replace(str_a.begin(), str_a.end(), ',', '.');
    replace(str_b.begin(), str_b.end(), ',', '.');
    float float_a=stof(str_a);
    float float_b=stof(str_b);
    int int_a=stoi(str_a);
    int int_b=stoi(str_b);

    if (float_a>float_b) return a;
    if (float_b>float_a) return b;
    if (int_a>int_b) return a;
    if (int_b>int_a) return b;
    return "None";
}

