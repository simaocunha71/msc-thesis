    float a1,b1;
    if (a.type()==typeid(string))
    a1=atof(a.c_str());
    else
    a1=boost::any_cast<float>(a);

    if (b.type()==typeid(string))
    b1=atof(b.c_str());
    else
    b1=boost::any_cast<float>(b);

    if (a1>b1)
    return a;
    if (b1>a1)
    return b;
    return "None";
}

