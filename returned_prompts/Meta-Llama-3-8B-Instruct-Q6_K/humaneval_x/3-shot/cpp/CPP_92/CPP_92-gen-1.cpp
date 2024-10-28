    if (abs(a-b-c)<0.0001 && a-b-c>0 && floor(a-b-c)==a-b-c)
    return true;
    if (abs(a-c-b)<0.0001 && a-c-b>0 && floor(a-c-b)==a-c-b)
    return true;
    if (abs(b-c-a)<0.0001 && b-c-a>0 && floor(b-c-a)==b-c-a)
    return true;
    return false;
}

