    sort(l.begin(), l.end());
    int n = l.size();
    if(n%2 != 0){
        return l[(n-1)/2];
    }
    else{
        return (l[n/2 - 1] + l[n/2])/2.0;
    }
}

int main(){
    vector<float> l1 = {3, 1, 2, 4, 5};
    vector<float> l2 = {-10, 4, 6, 1000, 10, 20};
    printf("%.1f\n", median(l1));
    printf("%.1f\n", median(l2));
    return 0;
}

*/

#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    sort(l.begin(), l.end());
    int n = l.size();
    if(n%2 != 0){
        return l[(n-1)/2];
    }
    else{
        return (l[n/2 - 1] + l[n/2])/2.0;
    }
}

int main(){
    vector<float> l1 = {3, 1, 2, 4, 5};
    vector<float> l2 = {-10, 4, 6, 1000, 10, 20};
    printf("%.1f\n", median(l1));
    printf("%.1f\n", median(l2));
    return 0;
}


/*
int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    sort(l.begin(), l.end());
    int n = l.size();
    if(n%2 != 0){
        printf("%.0f\n", l[(n-1)/2]);
    }
    else{
        printf("%.1f\n", (l[n/