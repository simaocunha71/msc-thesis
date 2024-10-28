    if (a.type() != b.type())
    return "None";
    if (a.type() == typeid(int)){
        int a_int=boost::any_cast<int>(a);
        int b_int=boost::any_cast<int>(b);
        if (a_int == b_int)
        return "None";
        if (a_int > b_int)
        return a;
        return b;
    }
    if (a.type() == typeid(float)){
        float a_float=boost::any_cast<float>(a);
        float b_float=boost::any_cast<float>(b);
        if (a_float == b_float)
        return "None";
        if (a_float > b_float)
        return a;
        return b;
    }
    if (a.type() == typeid(string)){
        string a_str=boost::any_cast<string>(a);
        string b_str=boost::any_cast<string>(b);
        if (a_str == b_str)
        return "None";
        if (a_str > b_str)
        return a;
        return b;
    }
    return "None";
}


