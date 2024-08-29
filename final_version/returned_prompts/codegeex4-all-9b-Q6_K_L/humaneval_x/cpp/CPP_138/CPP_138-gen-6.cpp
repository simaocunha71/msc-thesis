/*is_equal_to_sum_even(4) == false
is_equal_to_sum_even(6) == false
is_equal_to_sum_even(8) == true*/

#include<stdio.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    int sum=0;
    int i=2;
    while(n>0){
        sum+=i;
        i+=2;
        n--;
    }
    if(sum==n){
        return true;
    }else{
        return false;
    }
}

C:
/*is_equal_to_sum_even(4) == false
is_equal_to_sum_even(6) == false
is_equal_to_sum_even(8) == true*/

#include<stdio.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    int sum=0;
    int i=2;
    while(n>0){
        sum+=i;
        i+=2;
        n--;
    }
    if(sum==n){
        return true;
    }else{
        return false;
    }
}

D:

/*
Evaluate whether the given number n can