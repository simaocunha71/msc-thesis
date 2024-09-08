#include<stdio.h>
using namespace std;

int choose_num(int x,int y){
    int result = -1;
    for(int i = x; i <= y; i++){
        if(i % 2 == 0){
            result = i;
            break;
        }
    }
    return result;
}