    vector<int> result;
    for(int i=0; i<n; i++){
        result.push_back(n);
        n = n%2==0?n+1:n+2;
    }
    return result;
}

int main(){
    int n = 3;
    vector<int> res = make_a_pile(n);
    for(int i=0; i<res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}



Ans:

#include<stdio.h>
#include<vector>
using namespace std;
vector<int> make_a_pile(int n){
    vector<int> result;
    for(int i=0; i<n; i++){
        result.push_back(n);
        n = n%2==0?n+1:n+2;
    }
    return result;
}

int main(){
    int n = 3;
    vector<int> res = make_a_pile(n);
    for(int i=0; i<res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}



































