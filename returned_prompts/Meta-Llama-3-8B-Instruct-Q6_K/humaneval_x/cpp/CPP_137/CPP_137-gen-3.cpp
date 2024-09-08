boost::any compare_one(boost::any a,boost::any b){
    if(a.type() == typeid(int) && b.type() == typeid(int)){
        int x = boost::any_cast<int>(a);
        int y = boost::any_cast<int>(b);
        if(x > y) return a;
        else if(x < y) return b;
        else return boost::any("None");
    }
    else if(a.type() == typeid(double) && b.type() == typeid(double)){
        double x = boost::any_cast<double>(a);
        double y = boost::any_cast<double>(b);
        if(x > y) return a;
        else if(x < y) return b;
        else return boost::any("None");
    }
    else if(a.type() == typeid(string) && b.type() == typeid(string)){
        string x = boost::any_cast<string>(a);
        string y = boost::any_cast<string>(b);
        if(x > y) return a;
        else if(x < y) return b;
        else return boost::any("None");
    }
    else if(a.type() == typeid(int) && b.type() == typeid(double)){
        int x = boost::any_cast<int>(a);
        double y = boost::any_cast<double>(b);
        if(x > y) return a;
        else if(x < y) return b;
        else return boost::any("None");
    }
    else if(a.type() == typeid(double) && b.type() == typeid(int)){
        double x = boost::any_cast<double>(a);
        int y = boost::any_cast<int>(b);
        if(x > y) return a;
        else if(x < y) return b;
        else return boost::any("None");
    }
    else if(a.type() == typeid(string) && b.type() == typeid(int)){
        string x = boost::any_cast<string>(a);
        int y = boost::any_cast<int>(b);
        if(x > to_string(y)) return a;
        else if(x < to_string(y)) return b;
        else return boost::any("None");
    }
    else if(a.type() == typeid(int) && b.type() == typeid(string)){
        int x = boost::any_cast<int>(a);
        string y = boost::any_cast<string>(b);
        if(to_string(x) > y) return a;
        else if(to_string(x) <