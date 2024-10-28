    vector<int> result;

B:
    if(need<=remaining){
        result.push_back(number+need);
        result.push_back(remaining-need);
    }else{
        result.push_back(number+remaining);
        result.push_back(0);
    }

    return result;
}

int main(){
    int number,need,remaining;
    printf("Enter the number of carrots eaten, the need of carrots and the remaining carrots:\n");
    scanf("%d %d %d",&number,&need,&remaining);

    vector<int> result = eat(number,need,remaining);

    printf("Total number of eaten carrots after your meals: %d\n",result[0]);
    printf("Number of carrots left after your meals: %d\n",result[1]);

    return 0;
}
*/

#include<stdio.h>
#include<vector>
using namespace std;
vector<int> eat(int number,int need,int remaining){

    vector<int> result;

    if(need<=remaining){
        result.push_back(number+need);
        result.push_back(remaining-need);
    }else{
        result.push_back(number+remaining);
        result.push_back(0);
    }

    return result;
}

int main(){
    int number,need,remaining;
    printf("Enter the number of carrots eaten, the need of carrots and the remaining carrots:\n");
    scanf("%d %d %d",&number,&need,&remaining);

    vector<int> result = eat(number,need,remaining);

    printf("Total number of eaten carrots after your meals: %d\n",result[0]);
    printf("Number of carrots left after your meals: %d\n",result[1]);

    return 0;
}

//Test/Test.cpp
#include <gtest/gtest.h>
#include <vector>