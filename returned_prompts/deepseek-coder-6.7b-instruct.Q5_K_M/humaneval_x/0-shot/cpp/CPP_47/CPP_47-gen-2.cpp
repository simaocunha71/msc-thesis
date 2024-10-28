    sort(l.begin(), l.end());
    int n = l.size();
    if(n%2 == 0){
        return (l[n/2-1]+l[n/2])/2;
    }
    else{
        return l[n/2];
    }
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%f\n", median(l));
    l = {-10, 4, 6, 1000, 10, 20};
    printf("%f\n", median(l));
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
    if(n%2 == 0){
        return (l[n/2-1]+l[n/2])/2;
    }
    else{
        return l[n/2];
    }
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%f\n", median(l));
    l = {-10, 4, 6, 1000, 10, 20};
    printf("%f\n", median(l));
    return 0;
}

*/

// ----------------------------------

/*
