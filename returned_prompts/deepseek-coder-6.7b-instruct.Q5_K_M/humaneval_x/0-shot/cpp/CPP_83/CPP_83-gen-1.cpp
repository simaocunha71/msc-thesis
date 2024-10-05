    int count = 0;
    if(n == 1) return 2;
    else {
        for(int i = 1; i < n; i++){
            count += (9 * (pow(10, i-1))) + 2;
        }
    return count;
    }
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", starts_one_ends(n));
    return 0;
}
*/

#include <stdio.h>
#include <math.h>

int starts_one_ends(int n) {
    int count = 0;
    if(n == 1) return 2;
    else {
        for(int i = 1; i < n; i++){
            count += (9 * pow(10, i-1)) + 2;
        }
    return count;
    }
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", starts_one_ends(n));
    return 0;
}

//C++/starts_one_ends.cpp
/*
