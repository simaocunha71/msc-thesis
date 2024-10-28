    if (typeid(a)==typeid(int))
    if (typeid(b)==typeid(int))
    if (a<b)
    return b;
    else if (b<a)
    return a;
    else
    return "None";

    if (typeid(a)==typeid(float))
    if (typeid(b)==typeid(float))
    if (a<b)
    return b;
    else if (b<a)
    return a;
    else
    return "None";

    if (typeid(a)==typeid(string))
    if (typeid(b)==typeid(string))
    if (a<b)
    return b;
    else if (b<a)
    return a;
    else
    return "None";
}


