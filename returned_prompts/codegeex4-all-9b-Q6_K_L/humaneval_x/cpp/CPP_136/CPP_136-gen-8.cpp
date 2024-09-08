#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> v={0,0};
    int max=-10000000;
    int min=10000000;
    if(lst.size()==0){
        return v;
    }
    else{
        for(int i=0;i<lst.size();i++){
            if(lst[i]>0 && lst[i]<min){
                min=lst[i];
            }
            else if(lst[i]<0 && lst[i]>max){
                max=lst[i];
            }
        }
    }
    if(max==-10000000){
        max=0;
    }
    if(min==10000000){
        min=0;
    }
    return {max,min};
}

C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> v={0,0};
    int max=-10000000;
    int min=10000000;
    if(lst.size()==0){
        return v;
    }
    else{
        for(int i=0;i<lst.size();i++){
            if(lst[i]>0 && lst[i]<min){
                min=lst[i];
            }
            else if(lst[i]<0 && lst[i]>max){
                max=lst[i];
            }
        }
    }
    if(max==-10000000){
        max=0;
    }
    if(min==10000000){
        min=0;
    }
    return {max,min};
}

D:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> v={0,0};
    int max=-10000000;
    int min=10000000;
    if(lst.size()==0){
        return v;
    }
    else{
        for(int i=0;i<lst.size();i++){
            if(lst[i]>0 && lst[i]<min){
                min=lst[i];
            }
            else if(lst[i]<0 && lst[i]>max){
                max=lst[i];
            }
        }
    }
    if(max==-10000000){
        max=0;
    }
    if(min==10000000){
        min=0;
    }
    return {max,min};
}

E:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst