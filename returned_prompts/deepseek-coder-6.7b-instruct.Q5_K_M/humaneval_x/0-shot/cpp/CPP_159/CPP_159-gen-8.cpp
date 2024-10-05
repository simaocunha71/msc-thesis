    if(remaining >= need){
        int total = number + need;
        int left = 0;
        return {total, left};
    }
    else{
        int total = number + remaining;
        int left = need - remaining;
        return {total, left};
    }
}

int main(){
    int number,need,remaining;
    scanf("%d %d %d",&number,&need,&remaining);
    vector<int> result = eat(number,need,remaining);
    printf("The total number of eaten carrots is: %d\n", result[0]);
    printf("The number of carrots left is: %d\n", result[1]);
    return 0;
}

*/
#include<iostream>
#include<vector>
using namespace std;

vector<int> eat(int number, int need, int remaining){
    if(remaining >= need){
        return {number + need, 0};
    }
    else{
        return {number + remaining, need - remaining};
    }
}

int main(){
    int number, need, remaining;
    cin >> number >> need >> remaining;
    vector<int> result = eat(number, need, remaining);
    cout << "The total number of eaten carrots is: " << result[0] << endl;
    cout << "The number of carrots left is: " << result[1] << endl;
    return 0;
}

//RabbitEatsCarrots/test.cpp
#include<iostream>
#include<vector>
#include "RabbitEatsCarrots.cpp"
using namespace std;

int main(){
    int number, need, remaining;
    cin >> number >> need >> remaining;
    vector<int> result = eat(number, need, remaining);
    cout << "The total number of eaten carrots is: " << result[0] << endl;
    cout << "The number of carrots left is: " << result[1] << endl;
    return 0;
}

//RabbitEatsCarro