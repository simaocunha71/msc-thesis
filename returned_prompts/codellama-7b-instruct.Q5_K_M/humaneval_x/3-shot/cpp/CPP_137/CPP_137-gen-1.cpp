    if (a.type()==typeid(int) && b.type()==typeid(int)){
        int aa=a.as<int>();
        int bb=b.as<int>();
        if (aa>bb)
        return b;
        else if (bb>aa)
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(float) && b.type()==typeid(float)){
        float aa=a.as<float>();
        float bb=b.as<float>();
        if (aa>bb)
        return b;
        else if (bb>aa)
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(float) && b.type()==typeid(int)){
        float aa=a.as<float>();
        int bb=b.as<int>();
        if (aa>bb)
        return b;
        else if (bb>aa)
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(int) && b.type()==typeid(float)){
        int aa=a.as<int>();
        float bb=b.as<float>();
        if (aa>bb)
        return b;
        else if (bb>aa)
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(string) && b.type()==typeid(string)){
        string aa=a.as<string>();
        string bb=b.as<string>();
        if (aa>bb)
        return b;
        else if (bb>aa)
        return a;
        else
        return "None";
    }
    if (a.type()==typeid(string) && b.type()==typeid(int)){
        string aa=a.as<string>();
        int bb=b.as<int>();
        if (aa>bb)
        return b;
        else if (bb>aa)
        return a;
        else