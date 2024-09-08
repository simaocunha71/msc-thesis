#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){
    int sum=0;
    for(int i=0;i<n.size();i++){
        int num=n[i];
        int digit_sum=0;
        int sign=1;
        if(num<0){
            num=-num;
            sign=-1;
        }
        while(num>0){
            digit_sum+=num%10;
            num/=10;
        }
        sum+=digit_sum*sign;
    }
    if(sum>0){
        return 1;
    }else{
        return 0;
    }
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){
    int count=0;
    for(int i=0;i<n.size();i++){
        int num=n[i];
        int digit_sum=0;
        int sign=1;
        if(num<0){
            num=-num;
            sign=-1;
        }
        while(num>0){
            digit_sum+=num%10;
            num/=10;
        }
        if(digit_sum*sign>0){
            count++;
        }
    }
    return count;
}