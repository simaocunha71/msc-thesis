    if(n>m)
        return "-1";
    long long sum = 0;
    for(int i=n;i<=m;i++)
        sum += i;
    double avg = (double)sum/(m-n+1);
    avg = floor(avg+0.5); //round down to nearest integer
    string binary = "";
    while(avg>0){
        binary.push_back(avg%2+'0');
        avg /= 2;
    }
    reverse(binary.begin(),binary.end());
    return binary;
}

int main()
{
    cout << rounded_avg(1,5) << endl; //11
    cout << rounded_avg(7,5) << endl; //-1
    cout << rounded_avg(10,20) << endl; //1111
    cout << rounded_avg(20,33) << endl; //11010
    return 0;
}
B:
#include<bits/stdc++.h>
using namespace std;

string rounded_avg(int n,int m){
    if(n>m) return "-1";
    long long sum = 0;
    for(int i=n;i<=m;i++) sum += i;
    double avg = (double)sum/(m-n+1);
    avg = floor(avg+0.5); //round down to nearest integer
    string binary = "";
    while(avg>0){
        binary.push_back(avg%2+'0');
        avg /= 2;
    }
    reverse(binary.begin(),binary.end());
    return binary;
}

int main(){
    cout << rounded_avg(1,5) << endl; //11
    cout << rounded_avg(7,5) << endl; //-1
    cout << rounded_avg(10,20) << endl; //1111
    cout << rounded_avg(20,33) << endl; //11010
    return 0;
}
C:
#include<bits/stdc++.h>
using namespace std;

string rounded_avg(int n,int m){
    if(n>m) return "-1";
    long long sum = 0;
    for(int i=n;i<=m;i++) sum += i;
    double avg = (double)sum/(m-n+1);
    avg = floor(avg+0.5); //round down to nearest integer
    string binary = "";
    while(avg>0){
        binary.push_back(avg%2+'0');
        avg /= 2;
    }
    reverse(binary.begin(),binary.end());
    return binary;
}

int main(){
    cout << rounded