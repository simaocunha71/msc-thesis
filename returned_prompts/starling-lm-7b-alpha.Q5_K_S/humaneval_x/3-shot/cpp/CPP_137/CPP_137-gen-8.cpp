    if (typeid(a)==typeid(b))
    {
        if (a<b) return b;
        if (a>b) return a;
        return "None";
    }
    if (typeid(a)==typeid(int) && typeid(b)==typeid(float))
    {
        if ((boost::any_cast<int>(a))<boost::any_cast<float>(b)) return boost::any_cast<float>(b);
        if ((boost::any_cast<int>(a))>(boost::any_cast<float>(b))) return boost::any_cast<int>(a);
        return "None";
    }
    if (typeid(a)==typeid(int) && typeid(b)==typeid(string))
    {
        if ((boost::any_cast<int>(a))>(boost::any_cast<string>(b).size())) return boost::any_cast<string>(b);
        return boost::any_cast<int>(a);
    }
    if (typeid(a)==typeid(string) && typeid(b)==typeid(int))
    {
        if ((boost::any_cast<int>(b))>(boost::any_cast<string>(a).size())) return boost::any_cast<string>(a);
        return boost::any_cast<int>(b);
    }
    if (typeid(a)==typeid(string) && typeid(b)==typeid(string))
    {
        if (boost::any_cast<string>(a)<boost::any_cast<string>(b)) return boost::any_cast<string>(b);
        if (boost::any_cast<string>(a)>boost::any_cast<string>(b)) return boost::any_cast<string>(a);
        return "None";
    }
}


