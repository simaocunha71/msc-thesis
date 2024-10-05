    if (a.type() == typeid(int) && b.type() == typeid(int)){
        int a1 = boost::any_cast<int>(a);
        int b1 = boost::any_cast<int>(b);
        if (a1>b1)
        return a;
        else
        return b;
    }
    if (a.type() == typeid(float) && b.type() == typeid(float)){
        float a1 = boost::any_cast<float>(a);
        float b1 = boost::any_cast<float>(b);
        if (a1>b1)
        return a;
        else
        return b;
    }
    if (a.type() == typeid(string) && b.type() == typeid(string)){
        string a1 = boost::any_cast<string>(a);
        string b1 = boost::any_cast<string>(b);
        if (a1.compare(b1)>0)
        return a;
        else
        return b;
    }
    if (a.type() == typeid(string) && b.type() == typeid(float)){
        float b1 = boost::any_cast<float>(b);
        string a1 = boost::any_cast<string>(a);
        if (stof(a1)>b1)
        return a;
        else
        return b;
    }
    if (a.type() == typeid(float) && b.type() == typeid(string)){
        float a1 = boost::any_cast<float>(a);
        string b1 = boost::any_cast<string>(b);
        if (a1>stof(b1))
        return a;
        else
        return b;
    }
    return "None";
}


