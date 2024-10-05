    boost::any max;
    boost::any min;
    boost::any temp;
    float f1,f2;
    string s1,s2;
    if (a.type() == typeid(float) || a.type() == typeid(int))
    {
        if (b.type() == typeid(float) || b.type() == typeid(int))
        {
            f1=boost::any_cast<float>(a);
            f2=boost::any_cast<float>(b);
            max= (f1 > f2) ? a : b;
            min= (f1 < f2) ? a : b;
        }
    }
    else if (a.type() == typeid(string))
    {
        if (b.type() == typeid(string))
        {
            s1=boost::any_cast<string>(a);
            s2=boost::any_cast<string>(b);
            max= (stof(s1) > stof(s2)) ? a : b;
            min= (stof(s1) < stof(s2)) ? a : b;
        }
    }
    if (max.type() == typeid(float) || max.type() == typeid(int))
    {
        temp=max;
    }
    else if (max.type() == typeid(string))
    {
        temp=boost::any_cast<string>(max);
    }
    if (temp.type() == typeid(string) && temp==min)
    {
        return "None";
    }
    return temp;
}