/*
#include<stdio.h>
#include<vector>
using namespace std;
int search(vector<int> lst){

    for(int i=lst.size()-1;i>=0;i--){
        int count=0;
        for(int j=0;j<lst.size();j++){
            if(lst[i]==lst[j])
                count++;
        }
        if(count>=lst[i]){
            return lst[i];
        }
    }
    return -1;
}
int main(){
    vector<int> lst={3,3,3,3,3};
    printf("%d\n",search(lst));
}

*/


#include<stdio.h>
#include<vector>
using namespace std;
int search(vector<int> lst){
    for(int i=lst.size()-1;i>=0;i--){
        int count=0;
        for(int j=0;j<lst.size();j++){
            if(lst[i]==lst[j])
                count++;
        }
        if(count>=lst[i]){
            return lst[i];
        }
    }
    return -1;
}
int main(){
    vector<int> lst={3,3,3,3,3};
    printf("%d\n",search(lst));
}


























