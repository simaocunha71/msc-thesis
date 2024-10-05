    float s1=sqrt((a*a)+(b*b));
    float s2=sqrt((a*a)+(c*c));
    float s3=sqrt((b*b)+(c*c));
    if (s1==c || s2==b || s3==a)
    return true;
    else
    return false;
}

