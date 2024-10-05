    vector<int> result;
    if(need<=remaining){
        result.push_back(number+need);
        result.push_back(remaining-need);
    }
    else{
        result.push_back(number+remaining);
        result.push_back(0);
    }
    return result;
}

int main(){
    vector<int> result = eat(5, 6, 10);
    printf("{%d, %d}", result[0], result[1]);
    return 0;
}

Output:

{11, 4}

*/

#include<iostream>
#include<vector>
using namespace std;

vector<int> eat(int number, int need, int remaining){
    vector<int> result;
    if(need<=remaining){
        result.push_back(number+need);
        result.push_back(remaining-need);
    }
    else{
        result.push_back(number+remaining);
        result.push_back(0);
    }
    return result;
}

int main(){
    vector<int> result = eat(5, 6, 10);
    cout << "{" << result[0] << ", " << result[1] << "}" << endl;
    return 0;
}


/*
You"re a hungry rabbit, and you already have eaten a certain number of carrots,
but now you need to eat more carrots to complete the day's meals.
you should return a vector of 2 elements { total number of eaten carrots after your meals,
                                the number of carrots left after your meals }
if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

Example:
* eat(5, 6, 10)  -> {11, 4}
* eat(4, 8, 9)  -> {12, 1}
* eat(1, 10, 10) -> {11, 0}
* eat(2, 