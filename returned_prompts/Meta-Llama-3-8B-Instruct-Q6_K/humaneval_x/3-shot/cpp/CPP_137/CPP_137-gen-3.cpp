    boost::any result;
    if (a.type() == typeid(int) && b.type() == typeid(int))
    {
        int ai = boost::any_cast<int>(a);
        int bi = boost::any_cast<int>(b);
        if (ai > bi)
            result = a;
        else if (bi > ai)
            result = b;
        else
            result = boost::any("None");
    }
    else if (a.type() == typeid(float) && b.type() == typeid(float))
    {
        float af = boost::any_cast<float>(a);
        float bf = boost::any_cast<float>(b);
        if (af > bf)
            result = a;
        else if (bf > af)
            result = b;
        else
            result = boost::any("None");
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string))
    {
        string as = boost::any_cast<string>(a);
        string bs = boost::any_cast<string>(b);
        if (as > bs)
            result = a;
        else if (bs > as)
            result = b;
        else
            result = boost::any("None");
    }
    else
        result = "Invalid input";
    return result;
}