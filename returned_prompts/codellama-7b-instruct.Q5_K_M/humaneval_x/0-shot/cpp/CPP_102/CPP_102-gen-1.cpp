/*
This function takes two positive numbers x and y and returns the
biggest even integer number that is in the range [x, y] inclusive. If 
there's no such number, then the function should return -1.

For example:
choose_num(12, 15) = 14
choose_num(13, 12) = -1
*/
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){

    int i,num;

    for(i=x;i<=y;i++){

        if(i%2==0)
            num=i;
    }
    if(num==0)
        return -1;
    else
        return num;
}

int main(){

    int x,y;
    scanf("%d %d",&x,&y);
    printf("%d",choose_num(x,y));
}
