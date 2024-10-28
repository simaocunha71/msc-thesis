    sort(lst.begin(), lst.end());
    vector<int> res;
    while(!lst.empty()){
        res.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            res.push_back(lst.back());
            lst.pop_back();
        }
    }
    return res;
}
int main(){
    vector<int> v = {1, 2, 3, 4};
    vector<int> res = strange_sort_list(v);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

Output:
1 4 2 3

*/

#include<vector>
#include<algorithm>
using namespace std;

vector<int> strange_sort_vector(vector<int> vec){
    sort(vec.begin(), vec.end());
    vector<int> res;
    while(!vec.empty()){
        res.push_back(vec.front());
        vec.erase(vec.begin());
        if(!vec.empty()){
            res.push_back(vec.back());
            vec.pop_back();
        }
    }
    return res;
}

//Test Cases
#include<iostream>
int main(){
    vector<int> v = {1, 2, 3, 4};
    vector<int> res = strange_sort_vector(v);
    for(int i=0; i<res.size(); i++)
        cout<<res[i]<<" ";
    cout<<endl;

    v = {5, 5, 5, 5};
    res = strange_sort_vector(v);
    for(int i=0; i<res.size(); i++)
        cout<<res[i]<<" ";
    cout<<endl;

    v = {};
    res = strange_sort_vector(v);
    for(int i=0; i<res