    if(x%2==0)
    {
        if(y%2==0)
        {
            if(x<=y)
            {
                return y;
            }
            else
            {
                return -1;
            }
        }
        else if(y%2!=0)
        {
            if(x<=y)
            {
                return y-1;
            }
            else
            {
                return -1;
            }
        }
    }
    else if(x%2!=0)
    {
        if(y%2==0)
        {
            if(x<=y)
            {
                return x;
            }
            else
            {
                return -1;
            }
        }
        else if(y%2!=0)
        {
            if(x<=y)
            {
                return x;
            }
            else
            {
                return -1;
            }
        }
    }
    return 0;
}

int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    printf("%d",choose_num(x,y));
    return 0;
}


*/












































































































































































































