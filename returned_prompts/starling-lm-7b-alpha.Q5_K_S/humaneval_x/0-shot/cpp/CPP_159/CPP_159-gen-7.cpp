    if(need+number>remaining){
        int eat_remaining=remaining-number;
        vector<int> return_value={number+eat_remaining,remaining-eat_remaining};
        return return_value;
    }else{
        vector<int> return_value={number+need,remaining-need};
        return return_value;
    }
}

int main(){
    int number,need,remaining;
    scanf("%d%d%d",&number,&need,&remaining);
    vector<int> return_value=eat(number,need,remaining);
    printf("%d %d\n",return_value[0],return_value[1]);
    return 0;
}

*/

#include<bits/stdc++.h>
using namespace std;
vector<int> eat(int number,int need,int remaining){
    if(need+number>remaining){
        int eat_remaining=remaining-number;
        vector<int> return_value={number+eat_remaining,remaining-eat_remaining};
        return return_value;
    }else{
        vector<int> return_value={number+need,remaining-need};
        return return_value;
    }
}

int main(){
    int number,need,remaining;
    scanf("%d%d%d",&number,&need,&remaining);
    vector<int> return_value=eat(number,need,remaining);
    printf("%d %d\n",return_value[0],return_value[1]);
    return 0;
}























































































































