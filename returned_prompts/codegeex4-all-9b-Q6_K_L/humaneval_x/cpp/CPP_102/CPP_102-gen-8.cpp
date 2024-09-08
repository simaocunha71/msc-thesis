#include <iostream>
using namespace std;
int choose_num(int x, int y)
{
    if (x > y)
    {
        return -1;
    }
    int max = -1;
    for (int i = x; i <= y; i++)
    {
        if (i % 2 == 0)
        {
            max = i;
        }
    }
    return max;
}

C:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    if (x > y)
    {
        return -1;
    }
    for(int i=x;i<=y;i++){
        if(i%2==0){
            return i;
        }
    }
    return -1;
}

D:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){

    for(int i=x;i<=y;i++){
        if(i%2==0){
            return i;
        }
    }
    return -1;
}

E:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=-1;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            max=i;
        }
    }
    return max;
}

F:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    if (x > y)
    {
        return -1;
    }
    int max=-1;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            max=i;
        }
    }
    return max;
}

G:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=-1;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            max=i;
        }
    }
    return max;
}

H:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    if (x > y)
    {
        return -1;
    }
    for(int i=x;i<=y;i++){
        if(i%2==0){
            return i;
        }
    }
    return -1;
}

I:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    if (x > y)
    {
        return -1;
    }
    for(int i=x;i<=y;i++){
        if(i%2==0){
            return i;
        }
    }
    return -1;
