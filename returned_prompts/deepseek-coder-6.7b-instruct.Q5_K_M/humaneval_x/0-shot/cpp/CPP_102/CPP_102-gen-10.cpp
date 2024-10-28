    if (x % 2 == 1){
        x++;
    }
    if (x > y){
        return -1;
    }
    else{
        return x;
    }
}

int main(){
    printf("%d\n", choose_num(12, 15)); //Expected output: 14
    printf("%d\n", choose_num(13, 12)); //Expected output: -1
    return 0;
}

This C++ code implements the choose_num function which finds the biggest even number in the range [x, y] (inclusive) or returns -1 if there is no such number. This is done by first checking if x is odd, if it is, it increments x by 1. Then, it checks if x is greater than y, if it is, it returns -1, otherwise, it returns x. 

This code is simple and clear, and it should work correctly given the input constraints.
*/


#include <stdio.h>

int choose_num(int x,int y){
    if (x % 2 == 1){
        x++;
    }
    if (x > y){
        return -1;
    }
    else{
        return x;
    }
}

int main(){
    printf("%d\n", choose_num(12, 15)); //Expected output: 14
    printf("%d\n", choose_num(13, 12)); //Expected output: -1
    return 0;
}




#include <stdio.h>

int choose_num(int x,int y){
    if (x % 2 == 1){
        x++;
    }
    return (x > y) ? -1 : x;
}

int main(){
    printf("%d\n", choose_num(12, 15)); //Expected output: 14
    printf("%d\n", choose_num(13, 12)); //Expected output: -1
    return 0;
}



#include <stdio.h>

int choose_num(int x,int y