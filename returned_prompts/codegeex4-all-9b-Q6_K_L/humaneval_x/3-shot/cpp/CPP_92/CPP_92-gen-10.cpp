    if (abs(a)==abs(b)+abs(c))
    return true;
    if (abs(b)==abs(a)+abs(c))
    return true;
    if (abs(c)==abs(a)+abs(b))
    return true;
    return false;
}

