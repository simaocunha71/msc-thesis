def count_nums(n):
    count=0
    for i in n:
        temp=i
        sum=0
        while temp!=0:
            if temp<0:
                sum+=temp%10
                temp/=10
            else:
                sum+=abs(temp%10)
                temp/=10
        if sum>0:
            count+=1
    return count
print count_nums([1,2,3,-1,0,-2,-3])

B:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){

    int count=0;
    for(int i=0;i<n.size();i++){
        int temp=n[i];
        int sum=0;
        while(temp!=0){
            if(temp<0){
                sum+=temp%10;
                temp/=10;
            }else{
                sum+=abs(temp%10);
                temp/=10;
            }
        }
        if(sum>0){
            count+=1;
        }
    }
    return count;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){

    int count=0;
    for(int i=0;i<n.size();i++){
        int temp=n[i];
        int sum=0;
        while(temp!=0){
            if(temp<0){
                sum+=temp%10;
                temp/=10;
            }else{
                sum+=abs(temp%10);
                temp/=10;
            }
        }
        if(sum>0){
            count+=1;
        }
    }
    return count;
}

D:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){

    int count=0;
    for(int i=0;i<n.size();i++){
        int temp=n[i];
        int sum=0;
        while(temp!=0){
            if(temp<0){
                sum+=temp%10;
                temp/=10;
            }else{
                sum+=abs(temp%10);
                temp/=10;
            }
        }
        if(sum>0){
            count+=1;
        }
    }
    return count;
}

E:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){

    int count=0;
    for(int i=0;i<n.size();i++){
        int temp=n[i];
       