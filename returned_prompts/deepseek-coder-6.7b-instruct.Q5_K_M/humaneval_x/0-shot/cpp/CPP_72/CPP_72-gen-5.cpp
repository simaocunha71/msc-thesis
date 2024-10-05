    int sum = 0, n = q.size();
    for(int i = 0; i < n; i++){
        sum += q[i];
    }
    if(sum > w){
        return false;
    }
    int start = 0, end = n - 1;
    while(start < end){
        if(q[start] != q[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main(){
    printf("%d\n",will_it_fly({1, 2}, 5));
    printf("%d\n",will_it_fly({3, 2, 3}, 1));
    printf("%d\n",will_it_fly({3, 2, 3}, 9));
    printf("%d\n",will_it_fly({3}, 5));
    return 0;
}

*/

*/

#include<stdio.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum = 0, n = q.size();
    for(int i = 0; i < n; i++){
        sum += q[i];
    }
    if(sum > w){
        return false;
    }
    int start = 0, end = n - 1;
    while(start < end){
        if(q[start] != q[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main(){
    printf("%d\n",will_it_fly({1, 2}, 5));
    printf("%d\n",will_it_fly({3, 2, 3}, 1));
    printf("%d\n",will_it_fly({3, 2, 3}, 9));
    printf("%d\n",will_it_fly({3}, 5));
    return 0;
}

*/
// Output:
// 0
// 0
// 1