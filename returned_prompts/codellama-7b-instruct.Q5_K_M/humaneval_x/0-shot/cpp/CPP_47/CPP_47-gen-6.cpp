}



// Version 2
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    int n = l.size();
    sort(l.begin(), l.end());
    if (n%2==0) return (l[n/2]+l[n/2-1])/2.0;
    return l[n/2];
}



// Version 3
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    int n = l.size();
    if (n==0) return 0;
    sort(l.begin(), l.end());
    if (n%2==0) return (l[n/2]+l[n/2-1])/2.0;
    return l[n/2];
}



// Version 4
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    int n = l.size();
    if (n<0) return 0;
    sort(l.begin(), l.end());
    int m = (n+1)/2;
    if (m>=n) return l[n-1];
    return (l[m-1]+l[m])/2.0;
}



// Version 5
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
    int n = l.size();
    if (n<=0) return 0;
    sort(l.begin(), l.end());
    int m = (n+1)/2;
    if (m>=n) return l[n-1];
    return (l[m-1]+l[m])/2.0;
}



// Version 