    int a,b,c,d;
    stringstream ss1(x);
    ss1>>a>>"/">>b;
    stringstream ss2(n);
    ss2>>c>>"/">>d;
    if(a*d==b*c)
        return true;
    else
        return false;
}

int main()
{
    cout<<simplify("1/5", "5/1");
    return 0;
}

B:
    int a, b, c, d;
    stringstream ss1(x);
    ss1 >> a >> "/" >> b;
    stringstream ss2(n);
    ss2 >> c >> "/" >> d;
    int lcm = (b*d)/__gcd(b, d);
    int numerator = a * (d/lcm);
    int denominator = b * (d/lcm);
    return numerator == denominator;
}

C:
    int a, b, c, d;
    stringstream ss1(x);
    ss1 >> a >> "/" >> b;
    stringstream ss2(n);
    ss2 >> c >> "/" >> d;
    int gcd = __gcd(b, d);
    a *= d/gcd;
    b /= gcd;
    c *= d/gcd;
    d /= gcd;
    return a*b==c*d;
}

D:
    int a, b, c, d;
    stringstream ss1(x);
    ss1 >> a >> "/" >> b;
    stringstream ss2(n);
    ss2 >> c >> "/" >> d;
    int gcd = __gcd(b, d);
    a *= d/gcd;
    b /= gcd;
    c *= d/gcd;
    d /= gcd;
    return a*d==b*c;
}

E:
    int a, b, c, d;
    stringstream ss1(x);
    ss1 >> a >> "/" >> b;
    stringstream ss2(n);
    ss2 >> c >> "/" >> d;
    int lcm = (b*d)/__gcd(b, d);
    a *= d/lcm;
    b *= d/lcm;
    c *= b/lcm;
    d *= b/lcm;
    return a*d==c*b;
}

F:
    int a, b, c, d;
    stringstream ss1(x);
    ss1 >> a >> "/" >> b;
    stringstream ss2(n);
    ss2 >> c >> "/" >> d;
    int gcd = __gcd(b, d);
    a *= d/gcd;
    b /= gcd;
    c *= d