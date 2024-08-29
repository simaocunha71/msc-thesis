#include<stdio.h>
#include<vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    int min=0;
    int index=0;
    int flag=0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0){
            flag=1;
            if(arr[i]<min){
                min=arr[i];
                index=i;
            }
        }
    }
    if(flag==0)
        return {};
    else
        return {min,index};
}
B:
#include<stdio.h>
#include<vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    int min=0;
    int index=0;
    int flag=0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0){
            flag=1;
            if(arr[i]<min){
                min=arr[i];
                index=i;
            }
        }
    }
    return {min,index};
}
C:
#include<stdio.h>
#include<vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    int min=0;
    int index=0;
    int flag=0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0){
            flag=1;
            if(arr[i]<min){
                min=arr[i];
                index=i;
            }
        }
    }
    if(flag==0)
        return {};
    else
        return {min,index};
}
D:
#include<stdio.h>
#include<vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    int min=0;
    int index=0;
    int flag=0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0){
            flag=1;
            if(arr[i]<min){
                min=arr[i];
                index=i;
            }
        }
    }
    return {min,index};
}
E:
#include<stdio.h>
#include<vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    int min=0;
    int index=0;
    int flag=0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0){
            flag=1;
            if(arr[i]<min){
                min=arr[i];
                index=i;
            }
        }
    }
    return {min,index};
}
