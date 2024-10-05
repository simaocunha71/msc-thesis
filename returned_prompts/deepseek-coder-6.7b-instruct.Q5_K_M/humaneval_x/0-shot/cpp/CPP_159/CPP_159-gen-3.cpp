    vector<int> result;
    if(need > remaining){
        result.push_back(number + remaining);
        result.push_back(0);
    }else{
        result.push_back(number + need);
        result.push_back(remaining - need);
    }
    return result;
}

int main(){
    int number,need,remaining;
    scanf("%d %d %d",&number,&need,&remaining);
    vector<int> result = eat(number,need,remaining);
    printf("Total number of carrots eaten: %d\n",result[0]);
    printf("Remaining carrots: %d\n",result[1]);
    return 0;
}

*/

#include<stdio.h>
#include<vector>
using namespace std;
vector<int> eat(int number,int need,int remaining){
    vector<int> result;
    if(need > remaining){
        result.push_back(number + remaining);
        result.push_back(0);
    }else{
        result.push_back(number + need);
        result.push_back(remaining - need);
    }
    return result;
}

int main(){
    int number,need,remaining;
    scanf("%d %d %d",&number,&need,&remaining);
    vector<int> result = eat(number,need,remaining);
    printf("Total number of carrots eaten: %d\n",result[0]);
    printf("Remaining carrots: %d\n",result[1]);
    return 0;
}

/*
Note:
The problem is asking for a function that returns a vector with two integers. The first integer is the total number of carrots eaten, and the second integer is the number of carrots left.
If there are not enough carrots remaining, the function should eat all remaining carrots and return the total number of eaten carrots and 0 remaining carrots.
*/

// Code: End

// Solution: End

// Problem: End

// Solution: Begin
