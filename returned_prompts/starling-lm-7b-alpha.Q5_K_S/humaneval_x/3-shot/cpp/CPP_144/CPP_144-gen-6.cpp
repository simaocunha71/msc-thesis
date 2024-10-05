    int num1,num2,den1,den2;
    num1=atoi(x.c_str());
    den1=atoi(n.c_str());
    num2=atoi(n.c_str());
    den2=atoi(x.c_str());

    if (num1*den2==num2*den1)
    return true;
    return false;
}



