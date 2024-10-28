    if (abs(round(a)-a)<0.000001 && (b+c==a)) return true;
    if (abs(round(b)-b)<0.000001 && (a+c==b)) return true;
    if (abs(round(c)-c)<0.000001 && (a+b==c)) return true;
    return false;
}




