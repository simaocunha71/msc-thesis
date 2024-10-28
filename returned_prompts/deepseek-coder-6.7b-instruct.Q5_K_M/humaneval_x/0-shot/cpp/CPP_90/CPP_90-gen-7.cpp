    if(lst.size()<2){
        return NULL;
    }
    sort(lst.begin(), lst.end());
    for(int i=1; i<lst.size(); i++){
        if(lst[i]>lst[0]){
            return lst[i];
        }
    }
    return NULL;
}

int main(){
    vector<int> lst={1, 2, 3, 4, 5};
    printf("%d\n", next_smallest(lst));
    return 0;
}

*/

*/


// C++ Code
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int next_smallest(vector<int> lst){
    if(lst.size()<2){
        return NULL;
    }
    sort(lst.begin(), lst.end());
    for(int i=1; i<lst.size(); i++){
        if(lst[i]>lst[0]){
            return lst[i];
        }
    }
    return NULL;
}

int main(){
    vector<int> lst={1, 2, 3, 4, 5};
    cout << next_smallest(lst) << endl;
    return 0;
}
/*

*/


/*



*/



/*

*/























































































































































