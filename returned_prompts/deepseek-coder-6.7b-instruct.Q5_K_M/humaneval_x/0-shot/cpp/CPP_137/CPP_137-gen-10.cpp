    if (a.type() != typeid(b))
        return (a.type() > typeid(b)) ? a : b;

