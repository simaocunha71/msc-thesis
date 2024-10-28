    vector<int> result;

    for(int i=0; i<n; i++){
        if(n % 2 == 0)
            result.push_back(n + (2 * i));
        else
            result.push_back(n + (2 * i));
    }
    return result;
}

int main() {
    vector<int> result = make_a_pile(3);
    for(int i=0; i<result.size(); i++)
        printf("%d ", result[i]);
    return 0;
}

*/

#include<vector>
#include<iostream>
using namespace std;
vector<int> make_a_pile(int n){
    vector<int> result;
    for(int i=0; i<n; i++){
        if(n % 2 == 0)
            result.push_back(n + (2 * i));
        else
            result.push_back(n + (2 * i));
    }
    return result;
}

int main() {
    vector<int> result = make_a_pile(3);
    for(int i=0; i<result.size(); i++)
        cout<<result[i]<<" ";
    return 0;
}


/*
