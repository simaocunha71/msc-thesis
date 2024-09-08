#include<stdio.h>
using namespace std;

int choose_num(int x,int y){
    if(y-x==1)
    {
        return -1;
    }
    else if(y-x>1)
    {
        if(x%2==0)
        {
            return x;
        }
        else
        {
            x=x+1;
            return x;
        }
    }
    else
    {
        if(y%2==0)
        {
            return y;
        }
        else
        {
            y=y-1;
            return y;
        }
    }
}