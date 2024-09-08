#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    if(x==0){
        return false;
    }
    double k = log(x) / log(n);
    return k == floor(k);
}
