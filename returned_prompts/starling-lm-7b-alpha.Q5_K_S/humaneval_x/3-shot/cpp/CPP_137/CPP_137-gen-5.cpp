    if (typeid(a)==typeid(b)){
        if (typeid(a)==typeid(float) && typeid(b)==typeid(float))
        {
        if (a<b) return b;
        if (a>b) return a;
        return "None";
        }
        if (typeid(a)==typeid(int) && typeid(b)==typeid(int))
        {
        if (a<b) return b;
        if (a>b) return a;
        return "None";
        }
        if (typeid(a)==typeid(string) && typeid(b)==typeid(string))
        {
        if (a<b) return b;
        if (a>b) return a;
        return "None";
        }
    }
    if (typeid(a)==typeid(float)){
        if (a<b) return b;
        if (a>b) return a;
        return "None";
    }
    if (typeid(a)==typeid(int)){
        if (a<b) return b;
        if (a>b) return a;
        return "None";
    }
    if (typeid(a)==typeid(string)){
        if (a<b) return b;
        if (a>b) return a;
        return "None";
    }
}



