    if(floor(a)!=a||floor(b)!=b||floor(c)!=c)
    return false;
    if(a+b==c||a+c==b||b+c==a)
    return true;
    return false;
}

int main()
{
    printf("%d\n",any_int(5.0,2.0,7.0)); //true
    printf("%d\n",any_int(3.0,2.0,2.0)); //false
    printf("%d\n",any_int(3.0,-2.0,1.0)); //true
    printf("%d\n",any_int(3.6, -2.2, 2.0)); //false

    return 0;
}  */



