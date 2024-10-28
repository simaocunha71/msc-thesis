    string a_str, b_str;
    float a_float, b_float;
    int a_int, b_int;

    if(a.type() == typeid(int))
    {
        a_int = boost::any_cast<int>(a);
        b_int = boost::any_cast<int>(b);
        if(a_int > b_int)
            return a;
        if(a_int < b_int)
            return b;
    }

    if(a.type() == typeid(float))
    {
        a_float = boost::any_cast<float>(a);
        b_float = boost::any_cast<float>(b);
        if(a_float > b_float)
            return a;
        if(a_float < b_float)
            return b;
    }

    if(a.type() == typeid(string))
    {
        replace(a_str.begin(), a_str.end(), ',', '.');
        replace(b_str.begin(), b_str.end(), ',', '.');
        a_float = stof(a_str);
        b_float = stof(b_str);
        if(a_float > b_float)
            return a;
        if(a_float < b_float)
            return b;
    }
    return "None";
}

