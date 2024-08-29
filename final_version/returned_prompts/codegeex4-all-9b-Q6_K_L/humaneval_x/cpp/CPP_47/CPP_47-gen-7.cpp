    sort(l.begin(),l.end());
    if(l.size()%2==0){
        float mid1 = l[(l.size()-1)/2];
        float mid2 = l[l.size()/2];
        return (mid1+mid2)/2;
    }
    else
        return l[(l.size()-1)/2];
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f\n", median(l));
    l = {-10, 4, 6, 1000, 10, 20};
    printf("%.1f\n", median(l));
    return 0;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    sort(l.begin(),l.end());
    float mid = l[(l.size()-1)/2];
    return mid;
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f\n", median(l));
    l = {-10, 4, 6, 1000, 10, 20};
    printf("%.1f\n", median(l));
    return 0;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    sort(l.begin(),l.end());
    float mid1 = l[(l.size()-1)/2];
    float mid2 = l[l.size()/2];
    return (mid1+mid2)/2;
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f\n", median(l));
    l = {-10, 4, 6, 1000, 10, 20};
    printf("%.1f\n", median(l));
    return 0;
}

D:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    sort(l.begin(),l.end());
    float mid = l[(l.size()-1)/2];
    return mid;
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f\n", median(l));
    l = {-10, 4, 6