#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for (int i = 0; i < lst.size(); i++){
        if (lst[i] % 2 == 1 && lst[i] >= 0){
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}