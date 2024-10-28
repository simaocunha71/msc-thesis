    int num1,num2,den1,den2;
    sscanf(x.c_str(),"/%d/%d",&num1,&den1);
    sscanf(n.c_str(),"/%d/%d",&num2,&den2);
    return (num1*den2==num2*den1);
}


