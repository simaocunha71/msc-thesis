    if(a.type()==typeid(string) && b.type()==typeid(string)){
        string a_str=any_cast<string>(a);
        string b_str=any_cast<string>(b);
        a_str.erase(remove(a_str.begin(), a_str.end(), ','), a_str.end());
        b_str.erase(remove(b_str.begin(), b_str.end(), ','), b_str.end());
        float a_num=stof(a_str);
        float b_num=stof(b_str);
        if(a_num>b_num)
        return a;
        else if(b_num>a_num)
        return b;
        else 
        return "None";
    }
    else if(a.type()==typeid(float) && b.type()==typeid(float))
    {
        float a_num=any_cast<float>(a);
        float b_num=any_cast<float>(b);
        if(a_num>b_num)
        return a;
        else if(b_num>a_num)
        return b;
        else 
        return "None";
    }
    else if(a.type()==typeid(int) && b.type()==typeid(int))
    {
        int a_num=any_cast<int>(a);
        int b_num=any_cast<int>(b);
        if(a_num>b_num)
        return a;
        else if(b_num>a_num)
        return b;
        else
        return "None";
    }

    else 
    return "Error: Invalid input";

}


