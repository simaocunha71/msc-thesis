    float a1,b1;
    string a2,b2;
    if (a.type()==typeid(string))
    {
        a2=boost::any_cast<string>(a);
        replace(a2.begin(), a2.end(), ',', '.');
        a1=atof(a2.c_str());
    }
    if (b.type()==typeid(string))
    {
        b2=boost::any_cast<string>(b);
        replace(b2.begin(), b2.end(), ',', '.');
        b1=atof(b2.c_str());
    }
    if (a.type()==typeid(float) or a.type()==typeid(double))
        a1=boost::any_cast<float>(a);
    if (b.type()==typeid(float) or b.type()==typeid(double))
        b1=boost::any_cast<float>(b);
    if (a1>b1)
    return a1;
    if (a1<b1)
    return b1;
    if (a1==b1)
    return "None";
}

