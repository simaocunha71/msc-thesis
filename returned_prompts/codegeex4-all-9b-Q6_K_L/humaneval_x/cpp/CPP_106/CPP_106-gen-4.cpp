#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> f(int n){
    vector<int> vec;
    int fact = 1;
    int sum = 0;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            for(int j = 1; j <= i; j++){
                fact *= j;
            }
            vec.push_back(fact);
            fact = 1;
        }else{
            sum += i;
            vec.push_back(sum);
            sum = 0;
        }
    }
    return vec;
}

B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> f(int n){
    vector<int> vec;
    int fact = 1;
    int sum = 0;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            for(int j = 1; j <= i; j++){
                fact *= j;
            }
            vec.push_back(fact);
        }else{
            sum += i;
            vec.push_back(sum);
        }
    }
    return vec;
}

C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> f(int n){
    vector<int> vec;
    int fact = 1;
    int sum = 0;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            for(int j = 1; j <= i; j++){
                fact *= j;
            }
            vec.push_back(fact);
        }else{
            sum += i;
            vec.push_back(sum);
        }
    }
    return vec;
}

D:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> f(int n){
    vector<int> vec;
    int fact = 1;
    int sum = 0;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            for(int j = 1; j <= i; j++){
                fact *= j;
            }
            vec.push_back(fact);
        }else{
            sum += i;
            vec.push_back(sum);
        }
    }
    return vec;
}

E:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> f(int n){
    vector<int