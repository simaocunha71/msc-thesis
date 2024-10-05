    if(a.type()==typeid(int) && b.type()==typeid(int)){
        int a1=boost::any_cast<int>(a);
        int b1=boost::any_cast<int>(b);
        if(a1>b1)
            return a1;
        else if(b1>a1)
            return b1;
        else
            return boost::any("None");
    }
    else if(a.type()==typeid(float) && b.type()==typeid(float)){
        float a1=boost::any_cast<float>(a);
        float b1=boost::any_cast<float>(b);
        if(a1>b1)
            return a1;
        else if(b1>a1)
            return b1;
        else
            return boost::any("None");
    }
    else if(a.type()==typeid(string) && b.type()==typeid(string)){
        if(a.as<string>()>b.as<string>())
            return a.as<string>();
        else if(b.as<string>()>a.as<string>())
            return b.as<string>();
        else
            return boost::any("None");
    }
    else{
        if(a.type()==typeid(int) && b.type()==typeid(float)){
            int a1=boost::any_cast<int>(a);
            float b1=boost::any_cast<float>(b);
            if(a1>b1)
                return a1;
            else if(b1>a1)
                return b1;
            else
                return boost::any("None");
        }
        else if(a.type()==typeid(float) && b.type()==typeid(int)){
            int b1=boost::any_cast<int>(b);
            float a1=boost::any_cast<float>(a);
            if(a1>b1)
                return a1;
            else if(b1>a1)