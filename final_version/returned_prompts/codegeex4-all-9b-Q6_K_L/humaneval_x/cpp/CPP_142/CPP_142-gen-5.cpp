#include<stdio.h>
#include<vector>
using namespace std;

int sum_squares(vector<int> lst){
    int sum = 0;
    for (int i=0; i<lst.size(); i++){
        if (i%3==0){
            sum+=lst[i]*lst[i];
        }
        if (i%4==0 && i%3!=0){
            sum+=lst[i]*lst[i]*lst[i];
        }
    }
    return sum;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;

int sum_squares(vector<int> lst){
    int sum = 0;
    for (int i=0; i<lst.size(); i++){
        if (i%3==0){
            sum+=lst[i]*lst[i];
        }
        if (i%4==0 && i%3!=0){
            sum+=lst[i]*lst[i]*lst[i];
        }
    }
    return sum;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;

int sum_squares(vector<int> lst){
    int sum = 0;
    for (int i=0; i<lst.size(); i++){
        if (i%3==0){
            sum+=lst[i]*lst[i];
        }
        if (i%4==0 && i%3!=0){
            sum+=lst[i]*lst[i]*lst[i];
        }
    }
    return sum;
}

E:
#include<stdio.h>
#include<vector>
using namespace std;

int sum_squares(vector<int> lst){
    int sum = 0;
    for (int i=0; i<lst.size(); i++){
        if (i%3==0){
            sum+=lst[i]*lst[i];
        }
        if (i%4==0 && i%3!=0){
            sum+=lst[i]*lst[i]*lst[i];
        }
    }
    return sum;
}

