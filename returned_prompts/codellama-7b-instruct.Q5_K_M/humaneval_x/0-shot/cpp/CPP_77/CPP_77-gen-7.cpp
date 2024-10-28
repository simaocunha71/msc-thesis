    if(a==0)
    return true;
    if(a<0)
    {
        a=-a;
        goto A;
    }
    if(pow(a,1/3)==(int)pow(a,1/3))
    return true;
    return false;
}
int main(){

    int n;
    scanf("%d",&n);
    if(iscuber(n))
    printf("Yes");
    else
    printf("No");
    return 0;
}

Ans:
/*
Write a function that takes an integer a and returns true 
if this ingeger is a cube of some integer number.
Note: you may assume the input is always valid.
Examples:
iscube(1) ==> true
iscube(2) ==> false
iscube(-1) ==> true
iscube(64) ==> true
iscube(0) ==> true
iscube(180) ==> false
*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){

    if(a==0)
    return true;
    if(a<0)
    {
        a=-a;
        return iscuber(a);
    }
    if(pow(a,1/3)==(int)pow(a,1/3))
    return true;
    return false;
}
int main(){

    int n;
    scanf("%d",&n);
    if(iscuber(n))
    printf("Yes");
    else
    printf("No");
    return 0;
}

