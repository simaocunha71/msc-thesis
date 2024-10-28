    if(typeid(a)==typeid(b)){
        if(a==b)
        return "None";
        else if(typeid(a)==typeid(b)&&typeid(a)==typeid(int)){
            int a1=boost::any_cast<int>(a);
            int b1=boost::any_cast<int>(b);
            if(a1>b1)
            return a1;
            else return b1;
        }else if(typeid(a)==typeid(b)&&typeid(a)==typeid(float)){
            float a1=boost::any_cast<float>(a);
            float b1=boost::any_cast<float>(b);
            if(a1>b1)
            return a1;
            else return b1;
        }else if(typeid(a)==typeid(b)&&typeid(a)==typeid(string)){
            string a1=boost::any_cast<string>(a);
            string b1=boost::any_cast<string>(b);
            if(a1>b1)
            return a1;
            else return b1;
        }
    }else if(typeid(a)==typeid(int)&&typeid(b)==typeid(string)){
        int a1=boost::any_cast<int>(a);
        string b1=boost::any_cast<string>(b);
        float b11=atof(b1.c_str());
        if(a1>b11)
        return a1;
        else return b11;
    }else if(typeid(a)==typeid(string)&&typeid(b)==typeid(int)){
        string a1=boost::any_cast<string>(a);
        int b1=boost::any_cast<int>(b);
        float a11=atof(a1.c_str());
        if(a11>b1)
        return a11;
        else return b1;
    }else if(typeid(a)==typeid(string)&&typeid(b)==