    float sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        float diff = abs(numbers[i] - (float)numbers.size() / 2);
        sum += diff;
    }
    return sum / (float)numbers.size();
}
int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("%f\n", mean_absolute_deviation(numbers));
    return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin>>n;
    long long int i,j,k,l,m,r,t,x,y,z,sum=0,count=0;
    long long int a[n];
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int max = -1000000000;
    int min = 1000000000;
    for(i=0;i<n;i++)
    {
        if(a[i]>max)
        {
            max = a[i];
        }
        if(a[i]<min)
        {
            min = a[i];
        }
    }
    if(max-min<2)
    {
        cout<<"NO";
    }
    else
    {
        cout<<"YES";
    }
    return 0;
}



```
