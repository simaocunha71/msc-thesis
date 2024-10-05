    if (a.type()!=b.type())
    return "None";
    if (a.type()==typeid(int) || a.type()==typeid(float))
    {
        if (a<b)
        return b;
        else
        return a;
    }
    else
    {
        if (a<b)
        return b;
        else
        return a;
    }
}


