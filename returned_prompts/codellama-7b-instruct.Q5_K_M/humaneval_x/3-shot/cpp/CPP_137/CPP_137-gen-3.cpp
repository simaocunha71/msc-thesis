    if (a.type()==typeid(int)&&b.type()==typeid(int)){
        if (boost::any_cast<int>(a)<boost::any_cast<int>(b))
        return b;
        else if (boost::any_cast<int>(a)>boost::any_cast<int>(b))
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(float)&&b.type()==typeid(float)){
        if (boost::any_cast<float>(a)<boost::any_cast<float>(b))
        return b;
        else if (boost::any_cast<float>(a)>boost::any_cast<float>(b))
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(int)&&b.type()==typeid(float)){
        if (boost::any_cast<int>(a)<boost::any_cast<float>(b))
        return b;
        else if (boost::any_cast<int>(a)>boost::any_cast<float>(b))
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(float)&&b.type()==typeid(int)){
        if (boost::any_cast<float>(a)<boost::any_cast<int>(b))
        return b;
        else if (boost::any_cast<float>(a)>boost::any_cast<int>(b))
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(string)&&b.type()==typeid(string)){
        if (boost::any_cast<string>(a).length()<boost::any_cast<string>(b).length())
        return b;
        else if (boost::any_cast<string>(a).length()>boost::any_cast<string>(b).length())
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(string)&&b.type()