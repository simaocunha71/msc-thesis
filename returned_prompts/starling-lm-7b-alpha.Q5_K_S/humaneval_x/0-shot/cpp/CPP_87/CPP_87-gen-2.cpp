    vector<vector<int>> res;
    int i = 0;
    while(i < lst.size()){
        vector<int> tmp;
        int j = 0;
        while(j < lst[i].size()){
            if(lst[i][j] == x){
                tmp.push_back(i);
                tmp.push_back(j);
                j++;
            }else{
                j++;
            }
        }
        if(tmp.size() > 0){
            res.push_back(tmp);
        }
        i++;
    }
    res.erase(unique(res.begin(), res.end()), res.end());
    sort(res.begin(), res.end());
    return res;
}
int main(){
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    vector<vector<int>> res = get_row(lst, 1);
    for(int i = 0; i < res.size(); i++){
        for(int j = 0; j < res[i].size(); j++){
            printf("%d ", res[i][j]);
        }
        printf("\n");
    }
}


*/

#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> res;
    int i = 0;
    while(i < lst.size()){
        vector<int> tmp;
        int j = 0;
        while(j < lst[i].size()){
            if(lst[i][j] == x){
                tmp.push_back(i);
                tmp.push_back(j);
                j++;
            }else{
                j++;
            }
        }
        if(tmp.size() > 0){
            res.push_back(tmp);
        }