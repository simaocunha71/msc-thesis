    if (a==b)
    return "None";

    if (a.type()==typeid(int) && b.type()==typeid(int)){
        int a1=boost::any_cast<int>(a);
        int b1=boost::any_cast<int>(b);
        if (a1<b1)
        return b;
        if (a1>b1)
        return a;
    }
    if (a.type()==typeid(float) && b.type()==typeid(float)){
        float a1=boost::any_cast<float>(a);
        float b1=boost::any_cast<float>(b);
        if (a1<b1)
        return b;
        if (a1>b1)
        return a;
    }
    if (a.type()==typeid(string) && b.type()==typeid(string)){
        string a1=boost::any_cast<string>(a);
        string b1=boost::any_cast<string>(b);
        float a1_float=stof(a1);
        float b1_float=stof(b1);
        if (a1_float<b1_float)
        return b1;
        if (a1_float>b1_float)
        return a1;
    }
    return "None";
}



