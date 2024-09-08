#include<stdio.h>
#include<vector>
#include<map>
using namespace std;
int search(vector<int> lst){
    map<int,int> m;
    for(int i=0;i<lst.size();i++){
        m[lst[i]]++;
    }
    int max=0;
    for(auto it=m.begin();it!=m.end();it++){
        if(it->second >= it->first && it->first>max){
            max = it->first;
        }
    }
    return max>0?max:-1;
}

int main(){
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d\n",search(lst));
    lst = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    printf("%d\n",search(lst));
    lst = {5, 5, 4, 4, 4};
    printf("%d\n",search(lst));
    return 0;
}
