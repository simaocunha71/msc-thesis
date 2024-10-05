    if(x>y)
    {
        printf("x is bigger than y");
        return -1;
    }
    if(y%2!=0)
    {
        if(x%2!=0)
        {
            printf("odd");
            return -1;
        }
        else
        {
            if(y==x)
                return y;
            else
            {
                if(y-1==x)
                    return y-1;
                else
                    return -1;
            }
        }
    }
    else
        return y;
}


int main() {
    int x,y;
    scanf("%d%d",&x,&y);
    printf("%d",choose_num(x,y));
    return 0;
}

*/
























































































































































































































































































































