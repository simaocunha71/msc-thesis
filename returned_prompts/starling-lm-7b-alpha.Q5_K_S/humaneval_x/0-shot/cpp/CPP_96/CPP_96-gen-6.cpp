	if(n==0){
		vector<int> v;
		return v;
	}
	vector<int> v;
	if(n==1){
		v.push_back(2);
		return v;
	}
	if(n==2){
		v.push_back(2);
		return v;
	}
	v.push_back(2);
	v.push_back(3);
	for(int i=5;i<n;i+=2){
		int flag=0;
		for(int j=3;j<=(i/2);j++){
			if(i%j==0){
				flag=1;
				break;
			}
		}
		if(flag==0) v.push_back(i);
	}
	return v;
}
int main(){
	int n;
	scanf("%d",&n);
	vector<int> v = count_up_to(n);
	for(int i=0;i<v.size();i++)
		printf("%d ",v[i]);
	printf("\n");
	return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)

bool is_prime(int n){
    if(n==2) return true;
    if(n%2==0) return false;
    for(int i=3;i*i<=n;i+=2){
        if(n%i==0) return false;
    }
    return true;
}

vector<int> count_up_to(int n){
    vector<int> v;
    for(int i=2;i<n;i++){
        if(is_