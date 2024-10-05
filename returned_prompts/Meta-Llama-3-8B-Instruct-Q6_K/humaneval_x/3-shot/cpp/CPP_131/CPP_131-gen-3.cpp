    int product=1;
    string str;
    int i;
    str=to_string(n);
    for (i=0;i<str.length();i++)
    {
        if (str[i]-'0'%2!=0)
        product*=str[i]-'0';
    }
    return product;
} 
//or
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int product=1;
    while(n>0)
    {
        if (n%10%2!=0)
        product*=n%10;
        n=n/10;
    }
    return product;
}
//or
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int product=1;
    int temp=n;
    while(temp>0)
    {
        int digit=temp%10;
        if (digit%2!=0)
        product*=digit;
        temp=temp/10;
    }
    return product;
}
//or
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int product=1;
    while(n>0)
    {
        int digit=n%10;
        if (digit%2!=0)
        product*=digit;
        n=n/10;
    }
    return product;
}
//or
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int product=1;
    n=abs(n);
    while(n>0)
    {
        int digit=n%10;
        if (digit%2!=0)
        product*=digit;
        n=n/10;
    }
    return product;
} 
//or
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int product=1;
    n=abs(n);
    string str;
    str=to_string(n);
    for (int i=0;i<str.length();i++)
    {
        if (str[i]-'0'%2!=0)
        product*=str[i]-'0';
    }
    return product;
} 
//or
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int product=1;
    n=abs(n);
    while(n>0)
    {
        int digit=n%10;
        if (digit%2!=0)
        product*=digit;
        n=n/10;
    }
    return product;
} 
//or
#include<stdio.h>
#include<string>
using