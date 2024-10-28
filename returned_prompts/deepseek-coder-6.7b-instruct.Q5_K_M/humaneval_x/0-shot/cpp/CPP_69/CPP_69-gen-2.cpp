    int max_value = -1;
    int max_count = 0;
    int i, j;

B:
    for(i = 1; i <= *max_element(lst.begin(), lst.end()); i++){
        int count = 0;
        for(j = 0; j < lst.size(); j++){
            if(lst[j] == i){
                count++;
            }
        }
        if(count >= i && count > max_count){
            max_value = i;
            max_count = count;
        }
    }
    return max_value;
}


*/

#include<bits/stdc++.h>
using namespace std;

int search(vector<int> lst){
    int max_value = -1;
    int max_count = 0;
    int i, j;

    for(i = 1; i <= *max_element(lst.begin(), lst.end()); i++){
        int count = 0;
        for(j = 0; j < lst.size(); j++){
            if(lst[j] == i){
                count++;
            }
        }
        if(count >= i && count > max_count){
            max_value = i;
            max_count = count;
        }
    }
    return max_value;
}

int main(){
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    cout << search(lst) << endl;
    return 0;
}

/*
