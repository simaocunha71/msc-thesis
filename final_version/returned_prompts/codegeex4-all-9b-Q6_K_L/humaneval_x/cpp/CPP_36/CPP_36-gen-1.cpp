#include<stdio.h>
using namespace std;
int fizz_buzz(int n){
    int count=0;
    for(int i=0;i<n;i++)
    {
        if(i%11==0||i%13==0)
        {
            if(i%10==7)
                count++;
            if((i/10)%10==7)
                count++;
            if((i/100)%10==7)
                count++;
            if((i/1000)%10==7)
                count++;
            if((i/10000)%10==7)
                count++;
            if((i/100000)%10==7)
                count++;
            if((i/1000000)%10==7)
                count++;
            if((i/10000000)%10==7)
                count++;
            if((i/100000000)%10==7)
                count++;
            if((i/1000000000)%10==7)
                count++;
        }
    }
    return count;
}

B:
#include<stdio.h>
using namespace std;
int fizz_buzz(int n){
    int count=0;
    for(int i=0;i<n;i++)
    {
        if(i%11==0||i%13==0)
        {
            if(i%10==7)
                count++;
            if((i/10)%10==7)
                count++;
            if((i/100)%10==7)
                count++;
            if((i/1000)%10==7)
                count++;
            if((i/10000)%10==7)
                count++;
            if((i/100000)%10==7)
                count++;
            if((i/1000000)%10==7)
                count++;
            if((i/10000000)%10==7)
                count++;
            if((i/100000000)%10==7)
                count++;
            if((i/1000000000)%10==7)
                count++;
        }
    }
    return count;
}

C:
#include<stdio.h>
using namespace std;
int fizz_buzz(int n){
    int count=0;
    for(int i=0;i<n;i++)
    {
        if(i%11==0||i%13==0)
        {
            if(i%10==7)
                count++;
            if((i/10)%10==7)
                count++;
            if((i/100)%10==7)
                count++;
            if((i/100