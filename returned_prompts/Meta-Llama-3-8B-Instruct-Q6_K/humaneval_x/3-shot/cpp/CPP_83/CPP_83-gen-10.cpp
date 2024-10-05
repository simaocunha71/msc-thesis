    int count = 0;
    if (n==1)
        count = 9;
    else
    {
        count = 9 * (10^(n-1)) + 9 * (10^(n-2));
    }
    return count;
}
#include<vector>
using namespace std;
int ends_with_one(int n){
    int count = 0;
    if (n==1)
        count = 9;
    else
    {
        count = 10^(n-1) - 1;
    }
    return count;
}
#include<stdio.h>
using namespace std;
int count_numbers(int n){
    return starts_one_ends(n) + ends_with_one(n);
}  // This function counts the numbers that start or end with 1


