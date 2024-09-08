#include<stdio.h>
#include<math.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    for(int i=0;i<=n/2;i++){
        for(int j=0;j<=n/2;j++){
            for(int k=0;k<=n/2;k++){
                for(int l=0;l<=n/2;l++){
                    if(i%2==0&&j%2==0&&k%2==0&&l%2==0){
                        if(i+j+k+l==n){
                            return true;
                        }
                    }
                }
            }
        }
    }
    return false;
}