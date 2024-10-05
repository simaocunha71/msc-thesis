    for(int i=0; i<l.size(); i++){
        for(int j=i+1; j<l.size(); j++){
            if(l[i] + l[j] == 0){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 5, 7};
    vector<int> v5 = {1};
    printf("%d\n", pairs_sum_to_zero(v1));
    printf("%d\n", pairs_sum_to_zero(v2));
    printf("%d\n", pairs_sum_to_zero(v3));
    printf("%d\n", pairs_sum_to_zero(v4));
    printf("%d\n", pairs_sum_to_zero(v5));
    return 0;
}

O:
0
0
0
1
0
*/



#include<stdio.h>
#include<vector>
using namespace std;
bool pairs_sum_to_zero(vector<int> l){

    for(int i=0; i<l.size(); i++){
        for(int j=i+1; j<l.size(); j++){
            if(l[i] + l[j] == 0){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 5, 7};
   