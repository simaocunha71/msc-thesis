boost::any compare_one(boost::any a,boost::any b){
    if(a.type() == typeid(int) && b.type() == typeid(float)){
        int int_val = boost::any_cast<int>(a);
        float float_val = boost::any_cast<float>(b);
        if(int_val > float_val) return a;
        else return b;
    }
    else if(a.type() == typeid(float) && b.type() == typeid(int)){
        float float_val = boost::any_cast<float>(a);
        int int_val = boost::any_cast<int>(b);
        if(float_val > int_val) return a;
        else return b;
    }
    else if(a.type() == typeid(string) && b.type() == typeid(string)){
        string str1 = boost::any_cast<string>(a);
        string str2 = boost::any_cast<string>(b);
        if(str1 > str2) return a;
        else return b;
    }
    else if(a.type() == typeid(int) && b.type() == typeid(string)){
        int int_val = boost::any_cast<int>(a);
        string str = boost::any_cast<string>(b);
        if(to_string(int_val) > str) return a;
        else return b;
    }
    else if(a.type() == typeid(string) && b.type() == typeid(int)){
        string str = boost::any_cast<string>(a);
        int int_val = boost::any_cast<int>(b);
        if(str > to_string(int_val)) return a;
        else return b;
    }
    else if(a.type() == typeid(float) && b.type() == typeid(string)){
        float float_val = boost::any_cast<float>(a);
        string str = boost::any_cast<string>(b);
        if(to_string(float_val) > str) return a;
        else return b;
    }
    else if(a.type() == typeid(string) && b.type() == typeid(float)){
        string str = boost::any_cast<string>(a);
        float float_val = boost::any_cast<float>(b);
        if(str > to_string(float_val)) return a;
        else return b;
    }
    else if(a.type() == typeid(int) && b.type() == typeid(int)){
        int int_val1 = boost::any_cast<int>(a);
        int int_val2 = boost::any_cast<int>(b);
        if(int_val1 > int_val2) return a;
        else if