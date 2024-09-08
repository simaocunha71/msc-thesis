#include<stdio.h>
#include<math.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    if(n%2==0){
        int a,b,c,d;
        int s=0;
        for(a=1;a<=n-3;a+=2){
            for(b=a+2;b<=n-1;b+=2){
                for(c=b+2;c<=n-1;c+=2){
                    for(d=c+2;d<=n;d+=2){
                        s=a+b+c+d;
                        if(s==n){
                            return true;
                        }
                        else{
                            return false;
                        }
                    }
                }
            }
        }
    }
    return false;
}

B:
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    if(n%2==0){
        int a,b,c,d;
        int s=0;
        for(a=1;a<=n-3;a+=2){
            for(b=a+2;b<=n-1;b+=2){
                for(c=b+2;c<=n-1;c+=2){
                    for(d=c+2;d<=n;d+=2){
                        s=a+b+c+d;
                        if(s==n){
                            return true;
                        }
                        else{
                            return false;
                        }
                    }
                }
            }
        }
    }
    return false;
}

C:
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    if(n%2==0){
        int a,b,c,d;
        int s=0;
        for(a=1;a<=n-3;a+=2){
            for(b=a+2;b<=n-1;b+=2){
                for(c=b+2;c<=n-1;c+=2){
                    for(d=c+2;d<=n;d+=2){
                        s=a+b+c+d;
                        if(s==n){
                            return true;
                        }
                        else{
                            return false;
                        }
                    }
                }
            }
        }
    }
    return false;
}

D:
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    if(n%2==0){
        int a,b,c,d;
        int s=0;
        for(a=1;a<=n-3;a+=2){
            for(b=a+2;b<=n-1;b+=2){
                for(c=b+