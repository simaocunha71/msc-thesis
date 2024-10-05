    int sum = 0;
    int length = lst.size();
    for(int i = 0;i < length;i++){
        if(i % 3 == 0){
            lst[i] = lst[i] * lst[i];
        }
        if((i % 4 == 0) && (i % 3 != 0)){
            lst[i] = lst[i] * lst[i] * lst[i];
        }
        sum += lst[i];
    }
    return sum;
}

int main(){
    vector<int> lst;
    int result = sum_squares(lst);
    printf("%d\n",result);
    return 0;
}


*/
#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> lst = {1, 2, 3};
    cout << sum_squares(lst) << endl;
    return 0;
}

int sum_squares(vector<int> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (i % 3 == 0) {
            lst[i] = lst[i] * lst[i];
        }
        if ((i % 4 == 0) && (i % 3 != 0)) {
            lst[i] = lst[i] * lst[i] * lst[i];
        }
        sum += lst[i];
    }
    return sum;
}




/*
For lst = {-1,-5,2,-1,-5}  the output should be -126
For lst = {}  the output should be 0
For lst = {1,2,3} the output should be 6

Explanation
The function will not change the entries in the vector whose indexes are not a multiple of 3 or 4. So, the entries 2 and 5 will not be changed.
The function will square