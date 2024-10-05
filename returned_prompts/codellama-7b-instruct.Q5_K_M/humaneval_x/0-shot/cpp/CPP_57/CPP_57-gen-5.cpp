    for (int i=1; i<l.size(); i++){
        if (l[i] == l[i-1]){
            continue;
        }
        if (l[i] > l[i-1]){
            return true;
        }
        else{
            return false;
        }
    }
    return true;
}
int main(){
    vector<float> v = {1, 2, 4, 20};
    printf("%d\n", monotonic(v));
    v = {1, 20, 4, 10};
    printf("%d\n", monotonic(v));
    v = {4, 1, 0, -10};
    printf("%d\n", monotonic(v));
    return 0;
}

B:

#include<stdio.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
    for (int i=1; i<l.size(); i++){
        if (l[i] == l[i-1]){
            continue;
        }
        if (l[i] > l[i-1]){
            return true;
        }
        else{
            return false;
        }
    }
    return true;
}
int main(){
    vector<float> v = {1, 2, 4, 20};
    printf("%d\n", monotonic(v));
    v = {1, 20, 4, 10};
    printf("%d\n", monotonic(v));
    v = {4, 1, 0, -10};
    printf("%d\n", monotonic(v));
    return 0;
}

C:

#include<stdio.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
    for (int i=1; i<l.size(); i++){
        if (l[i] == l[i-1]){
            continue;
        }
        if (l[i] > l[i-1]){
