    string result;

    if(a.type() == typeid(int) && b.type() == typeid(float)){
        if(any_cast<int>(a) > any_cast<float>(b))
            return any_cast<int>(a);
        else
            return any_cast<float>(b);
    }
    else if(a.type() == typeid(float) && b.type() == typeid(float)){
        if(any_cast<float>(a) > any_cast<float>(b))
            return any_cast<float>(a);
        else
            return any_cast<float>(b);
    }
    else if(a.type() == typeid(string) && b.type() == typeid(string)){
        if(any_cast<string>(a) > any_cast<string>(b))
            return any_cast<string>(a);
        else
            return any_cast<string>(b);
    }
    else if(a.type() == typeid(int) && b.type() == typeid(int)){
        if(any_cast<int>(a) > any_cast<int>(b))
            return any_cast<int>(a);
        else if(any_cast<int>(a) == any_cast<int>(b))
            return "None";
        else
            return any_cast<int>(b);
    }
    else if(a.type() == typeid(int) && b.type() == typeid(string)){
        if(any_cast<int>(a) > stof(any_cast<string>(b)))
            return any_cast<int>(a);
        else if(any_cast<int>(a) == stof(any_cast<string>(b)))
            return "None";
        else
            return any_cast<string>(b);
    }
    else if(a.type() == typeid(string) && b.type() == typeid(int)){
        if(stof(any_cast<string>(a)) > any_cast<