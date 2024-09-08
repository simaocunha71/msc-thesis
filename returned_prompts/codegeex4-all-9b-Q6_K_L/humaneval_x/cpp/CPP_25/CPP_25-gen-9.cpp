#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
    vector<int> factors;
    int count = 0;
    for(int i = 2; i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n = n / i;
        }
    }
    return factors;
}
B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
    vector<int> factors;
    int count = 0;
    for(int i = 2; i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n = n / i;
            count++;
        }
        count = 0;
    }
    return factors;
}
C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
    vector<int> factors;
    int count = 0;
    for(int i = 2; i <= n; i++){
        if(n % i == 0){
            factors.push_back(i);
            n = n / i;
            count++;
        }
        count = 0;
    }
    return factors;
}
D:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
    vector<int> factors;
    for(int i = 2; i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n = n / i;
        }
    }
    return factors;
}

E:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
    vector<int> factors;
    int count = 0;
    for(int i = 2; i <= n; i++){
        if(n % i == 0){
            factors.push_back(i);
            n = n / i;
            count++;
        }
    }
    return factors;
}

F:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
    vector<int> factors;
    for(int i = 2; i <= n; i++){
        if(n % i == 0){
            factors.push_back(i);
            n = n / i;
        }
    }
    return factors;
}
G:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
    vector<int> factors;
    for(int i = 