#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
int closest_integer(string value){
    double num = atof(value.c_str());
    int res = round(num);
    if(num - res < 0.5){
        return res;
    }else{
        if(num > 0){
            return res+1;
        }else{
            return res-1;
        }
    }
}