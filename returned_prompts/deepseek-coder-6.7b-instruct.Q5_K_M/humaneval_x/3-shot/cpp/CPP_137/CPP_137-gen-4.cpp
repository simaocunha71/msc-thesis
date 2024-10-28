    if(a.type() == typeid(int) && b.type() == typeid(float)){
        return b;
    }
    else if(a.type() == typeid(float) && b.type() == typeid(int)){
        return a;
    }
    else if(a.type() == typeid(string) && b.type() == typeid(string)){
        string a_str = boost::any_cast<string>(a);
        string b_str = boost::any_cast<string>(b);

        // Removing ',' from numbers
        a_str.erase(remove(a_str.begin(), a_str.end(), ','), a_str.end());
        b_str.erase(remove(b_str.begin(), b_str.end(), ','), b_str.end());

        float a_float = stof(a_str);
        float b_float = stof(b_str);

        if(a_float > b_float)
            return a;
        else if(a_float < b_float)
            return b;
    }
    else if(a.type() == typeid(int) && b.type() == typeid(int)){
        if(boost::any_cast<int>(a) == boost::any_cast<int>(b))
            return "None";
        else if(boost::any_cast<int>(a) > boost::any_cast<int>(b))
            return a;
        else
            return b;
    }
    else if(a.type() == typeid(float) && b.type() == typeid(float)){
        if(boost::any_cast<float>(a) == boost::any_cast<float>(b))
            return "None";
        else if(boost::any_cast<float>(a) > boost::any_cast<float>(b))
            return a;
        else
            return b;
    }
    else if(a.type() == typeid(string) && b.type() == typeid(int)){
        string b_str = to_string