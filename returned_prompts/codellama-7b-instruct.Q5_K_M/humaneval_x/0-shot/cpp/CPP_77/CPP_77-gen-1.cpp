if(a<0)
{
    a=-a;
    goto A;
}
if((pow(a,1/3))==(int)pow(a,1/3))
{
    return 1;
}
else
{
    return 0;
}
}

int main()
{
    int a;
    while(scanf("%d",&a)!=EOF)
    {
        if(iscuber(a))
            printf("true\n");
        else
            printf("false\n");
    }
    return 0;
}

Explanation:
Note that the input is always valid.

First, the input is always positive.

Then, the cube of an integer is always an integer.

So, the function iscube(a) will return true if and only if a is a cube of some integer.

In the function, we first check if a is negative. If yes, we reverse the sign of a and return the result.

