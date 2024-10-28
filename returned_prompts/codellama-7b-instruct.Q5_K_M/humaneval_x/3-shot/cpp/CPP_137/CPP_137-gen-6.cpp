    float x=0.0,y=0.0;
    string sx,sy;
    if (a.type()==typeid(int)&&b.type()==typeid(float))
    {
        y=b.as<float>();
        x=a.as<int>();
    }
    else if (a.type()==typeid(float)&&b.type()==typeid(int))
    {
        y=a.as<float>();
        x=b.as<int>();
    }
    else if (a.type()==typeid(int)&&b.type()==typeid(int))
    {
        x=a.as<int>();
        y=b.as<int>();
    }
    else if (a.type()==typeid(float)&&b.type()==typeid(float))
    {
        x=a.as<float>();
        y=b.as<float>();
    }
    else if (a.type()==typeid(string)&&b.type()==typeid(string))
    {
        sx=a.as<string>();
        sy=b.as<string>();
    }
    

    if (y>x)
    return b;
    else if (x>y)
    return a;
    else
    return "None";
}



