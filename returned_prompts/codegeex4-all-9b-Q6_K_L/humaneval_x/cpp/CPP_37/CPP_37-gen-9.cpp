    vector<float> l1;  //存放偶数
    vector<float> l2;  //存放奇数
    vector<float> l3;  //存放结果
    int len = l.size();
    for(int i = 0; i < len; i++){
        if(i % 2 == 0){
            l1.push_back(l[i]);
        }else{
            l2.push_back(l[i]);
        }
    }
    sort(l1.begin(), l1.end());    //将偶数排序
    for(int i = 0; i < len; i++){
        if(i % 2 == 0){
            l3.push_back(l1[i]);
        }else{
            l3.push_back(l2[i]);
        }
    }
    return l3;
}

int main(){
    vector<float> l = {5, 6, 3, 4};
    vector<float> l1 = sort_even(l);
    for(int i = 0; i < l1.size(); i++){
        printf("%f ", l1[i]);
    }
    return 0;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<float> sort_even(vector<float> l){

C:
    vector<float> l1;  //存放偶数
    vector<float> l2;  //存放奇数
    vector<float> l3;  //存放结果
    int len = l.size();
    for(int i = 0; i < len; i++){
        if(i % 2 == 0){
            l1.push_back(l[i]);
        }else{
            l2.push_back(l[i]);
        }
    }
    sort(l1.begin(), l1.end());    //将偶数排序
    for(int i = 0; i < len; i++){
        if(i % 2 == 0){
            l3.push_back(l1[i]);
        }else{
            l3.push_back(l2[i]);
        }
    }
    return l3;
}

int main(){
    vector<float> l = {5, 6, 3, 4};
    vector<float> l1 = sort_even(l);
    for(int i = 0; i < l1.size(); i++){
        printf("%f ", l1[i]);
    }
    return 0;
}

D:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
