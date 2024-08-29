/*
#include<iostream>
#include<vector>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n = n / 2;
        }else{
            n = n * 3 + 1;
            res.push_back(n);
        }
    }
    res.push_back(1);
    return res;
}
*/

B:
/*
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n = n / 2;
        }else{
            n = n * 3 + 1;
            res.push_back(n);
        }
    }
    res.push_back(1);
    sort(res.begin(), res.end());
    return res;
}
*/

C:
/*
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n = n / 2;
        }else{
            n = n * 3 + 1;
            res.push_back(n);
        }
    }
    sort(res.begin(), res.end());
    res.push_back(1);
    return res;
}
*/

D:
/*
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n = n / 2;
        }else{
            n = n * 3 + 1;
        }
        res.push_back(n);
    }
    sort(res.begin(), res.end());
    return res;
}
*/

E:
/*
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n = n / 2;
        }else{
            n = n * 3 + 1;
        }
        res.push_back(n);
    }
    res.push_back(1);
    sort(res.begin(), res.end());
    return res;
}
*/

F:
/*
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector