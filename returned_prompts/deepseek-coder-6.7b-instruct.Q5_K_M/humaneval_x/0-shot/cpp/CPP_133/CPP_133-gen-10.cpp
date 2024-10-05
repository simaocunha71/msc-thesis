    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4,4.2,0};
    printf("%d", sum_squares(lst));
    return 0;
}

*/

#include<bits/stdc++.h>
using namespace std;

int sum_squares(vector<float>& lst){

    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4,4.2,0};
    printf("%d", sum_squares(lst));
    return 0;
}




// 