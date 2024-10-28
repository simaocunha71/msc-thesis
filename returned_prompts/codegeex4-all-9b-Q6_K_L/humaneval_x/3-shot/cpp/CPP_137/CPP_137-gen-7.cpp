    float a1,b1;
    string a2,b2;
    boost::any a3;
    if (a.type()==typeid(string))
    {
        a2=boost::any_cast<string>(a);
        boost::replace_all(a2, ",", ".");
        a1=atof(a2.c_str());
    }
    else
    a1=boost::any_cast<float>(a);
    if (b.type()==typeid(string))
    {
        b2=boost::any_cast<string>(b);
        boost::replace_all(b2, ",", ".");
        b1=atof(b2.c_str());
    }
    else
    b1=boost::any_cast<float>(b);
    if (a1<b1)
    {
        a3=b;
    }
    else if (a1>b1)
    {
        a3=a;
    }
    else
    {
        a3=boost::none;
    }
    return a3;
}

