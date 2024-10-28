    double A1=0.0;
    double B1=0.0;
    if (a.type()==typeid(string))
    {
        string a1=boost::any_cast<string>(a);
        replace(a1.begin(),a1.end(),',','.');
        A1=stod(a1);
    }
    if (b.type()==typeid(string))
    {
        string b1=boost::any_cast<string>(b);
        replace(b1.begin(),b1.end(),',','.');
        B1=stod(b1);
    }
    if (a.type()==typeid(int))
    A1=boost::any_cast<int>(a);
    if (b.type()==typeid(int))
    B1=boost::any_cast<int>(b);
    if (a.type()==typeid(float))
    A1=boost::any_cast<float>(a);
    if (b.type()==typeid(float))
    B1=boost::any_cast<float>(b);
    if (A1==B1)
    return boost::none;
    return A1>B1 ? a:b;
}

