    sort(l.begin(), l.end());
    if(l.size() % 2 == 0){
        return (l[l.size()/2] + l[l.size()/2-1])/2;
    }
    else{
        return l[l.size()/2];
    }
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f", median(l));
    return 0;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){

B:
    sort(l.begin(), l.end());
    if(l.size() % 2 == 0){
        return (l[l.size()/2] + l[l.size()/2-1])/2;
    }
    else{
        return (l[l.size()/2] + l[l.size()/2-1])/2;
    }
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f", median(l));
    return 0;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){

C:
    sort(l.begin(), l.end());
    if(l.size() % 2 == 0){
        return (l[l.size()/2] + l[l.size()/2-1])/2;
    }
    else{
        return l[l.size()/2+1];
    }
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f", median(l));
    return 0;
}

D:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){

D:
    sort(l.begin(), l.end());
    if(l.size() % 2 == 0){
        return (l[l.size()/2] + l[l.size()/2])/2;
    }
    else{
        return l[l.size()/2];
    }
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f", median(l));
    return 0;
}

E:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){

E:
