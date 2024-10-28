    string res;
    if(a.type()==typeid(int)){
        if(boost::any_cast<int>(a)>boost::any_cast<int>(b))
            return boost::any_cast<int>(a);
        else if(boost::any_cast<int>(a)<boost::any_cast<int>(b))
            return boost::any_cast<int>(b);
        else
            return "None";
    }
    else if(a.type()==typeid(float)){
        if(boost::any_cast<float>(a)>boost::any_cast<float>(b))
            return boost::any_cast<float>(a);
        else if(boost::any_cast<float>(a)<boost::any_cast<float>(b))
            return boost::any_cast<float>(b);
        else
            return "None";
    }
    else if(a.type()==typeid(string)){
        res = *max_element(a.begin(), a.end());
        if(res>*max_element(b.begin(), b.end()))
            return res;
        else if(res<*max_element(b.begin(), b.end()))
            return *max_element(b.begin(), b.end());
        else
            return "None";
    }
}


