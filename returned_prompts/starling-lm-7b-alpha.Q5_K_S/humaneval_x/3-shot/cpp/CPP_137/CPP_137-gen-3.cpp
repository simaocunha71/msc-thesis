    if (a.type()==typeid(int))
    if (b.type()==typeid(int))
    if (a<b) return b;
    if (a>b) return a;
    if (a.type()==typeid(float))
    if (b.type()==typeid(float))
    if (a<b) return b;
    if (a>b) return a;
    if (a.type()==typeid(string))
    if (b.type()==typeid(string))
    if (a<b) return b;
    if (a>b) return a;
    return "None";
}




