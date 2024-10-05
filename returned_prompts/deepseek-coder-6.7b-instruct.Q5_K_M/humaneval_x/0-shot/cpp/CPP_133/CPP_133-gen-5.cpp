    int sum = 0;

B:
    for(int i = 0; i < lst.size(); i++){

C:
        lst[i] = ceil(lst[i]);

D:
        sum += pow(lst[i], 2);
    }

E:
    return sum;
}

F:
int main(){
    vector<float> lst = {1.4, 4.2, 0};
    printf("%d\n", sum_squares(lst));
    return 0;
}

*/

#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

int sum_squares(vector<float> lst){
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4, 4.2, 0};
    cout<<sum_squares(lst)<<endl;
    return 0;
}






//end

//src/15-coding-bat/38-vector-1/sum3.cpp
/*
