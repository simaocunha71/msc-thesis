    vector<int> res;
    res.push_back(number);
    res.push_back(remaining);
    if(number + remaining >= need){
        int temp = need - number;
        res[0] += temp;
        res[1] = remaining - temp;
    }else{
        res[1] = 0;
        goto A;
    }
    return res;
}

*/

#include<stdio.h>
#include<vector>
using namespace std;

vector<int> eat(int number,int need,int remaining){
    vector<int> res;
    res.push_back(number);
    res.push_back(remaining);
    if(number + remaining >= need){
        int temp = need - number;
        res[0] += temp;
        res[1] = remaining - temp;
    }else{
        res[1] = 0;
    }
    return res;
}

int main(){
    vector<int> r = eat(2,11,5);
    printf("%d %d\n",r[0],r[1]);
    return 0;
}








































































































































































































































