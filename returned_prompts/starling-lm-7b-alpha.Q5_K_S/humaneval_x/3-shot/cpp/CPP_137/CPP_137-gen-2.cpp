    if (a.type()==typeid(int) && b.type()==typeid(int))
    {
    if (a<b) return b;
    if (a==b) return "None";
    return a;
    }
    if (a.type()==typeid(float) && b.type()==typeid(float))
    {
    if (a<b) return b;
    if (a==b) return "None";
    return a;
    }
    if (a.type()==typeid(string) && b.type()==typeid(string))
    {
    if (a<b) return b;
    if (a==b) return "None";
    return a;
    }
    if (a.type()==typeid(string) && b.type()==typeid(int))
    {
    int temp_int;
    string temp_str;
    boost::any temp;
    temp_str=(string)a;
    temp_int=(int)b;
    if (atoi(temp_str.c_str())<temp_int) return temp_int;
    if (atoi(temp_str.c_str())==temp_int) return "None";
    return temp_str;
    }
    if (a.type()==typeid(int) && b.type()==typeid(string))
    {
    int temp_int;
    string temp_str;
    boost::any temp;
    temp_int=(int)a;
    temp_str=(string)b;
    if (temp_int<atoi(temp_str.c_str())) return temp_str;
    if (temp_int==atoi(temp_str.c_str())) return "None";
    return temp_int;
    }
    return a;
}


