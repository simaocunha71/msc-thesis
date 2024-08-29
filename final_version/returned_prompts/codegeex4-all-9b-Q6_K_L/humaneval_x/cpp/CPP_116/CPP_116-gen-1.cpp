#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> arr){
    vector<int> result;
    sort(arr.begin(), arr.end(), [](int a, int b){
        int count_a = 0, count_b = 0;
        for(int i = 0; i < sizeof(a) * 8; i++){
            if((a & (1 << i)) != 0){
                count_a++;
            }
        }
        for(int i = 0; i < sizeof(b) * 8; i++){
            if((b & (1 << i)) != 0){
                count_b++;
            }
        }
        if(count_a == count_b){
            return a < b;
        }else{
            return count_a < count_b;
        }
    });
    return arr;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> arr){
    vector<int> result;
    sort(arr.begin(), arr.end(), [](int a, int b){
        int count_a = 0, count_b = 0;
        for(int i = 0; i < sizeof(a) * 8; i++){
            if((a & (1 << i)) != 0){
                count_a++;
            }
        }
        for(int i = 0; i < sizeof(b) * 8; i++){
            if((b & (1 << i)) != 0){
                count_b++;
            }
        }
        if(count_a == count_b){
            return a < b;
        }else{
            return count_a < count_b;
        }
    });
    return arr;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> arr){
    vector<int> result;
    sort(arr.begin(), arr.end(), [](int a, int b){
        int count_a = 0, count_b = 0;
        for(int i = 0; i < sizeof(a) * 8; i++){
            if((a & (1 << i)) != 0){
                count_a++;
            }
        }
        for(int i = 0; i < sizeof(b) * 8; i++){
            if((b & (1 << i)) != 0){
                count_b++;
            }
        }
