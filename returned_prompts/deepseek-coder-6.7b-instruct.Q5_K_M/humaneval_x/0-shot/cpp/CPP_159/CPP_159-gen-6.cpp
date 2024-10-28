    int total,left;
    if(need<=remaining){
        total=number+need;
        left=remaining-need;
    }
    else{
        total=number+remaining;
        left=0;
    }
    vector<int> result={total,left};
    return result;
}

int main() {
    vector<int> result=eat(5,6,10);
    printf("%d %d\n",result[0],result[1]);
    result=eat(4,8,9);
    printf("%d %d\n",result[0],result[1]);
    result=eat(1,10,10);
    printf("%d %d\n",result[0],result[1]);
    result=eat(2,11,5);
    printf("%d %d\n",result[0],result[1]);
    return 0;
}
*/

//C++/RabbitEatCarrots/main.cpp
#include "eat.cpp"
#include<iostream>
using namespace std;

int main() {
    vector<int> result=eat(5,6,10);
    cout<<result[0]<<" "<<result[1]<<endl;
    result=eat(4,8,9);
    cout<<result[0]<<" "<<result[1]<<endl;
    result=eat(1,10,10);
    cout<<result[0]<<" "<<result[1]<<endl;
    result=eat(2,11,5);
    cout<<result[0]<<" "<<result[1]<<endl;
    return 0;
}

//C++/RabbitEatCarrots/test.cpp
#include "eat.cpp"
#include<iostream>
using namespace std;

int main() {
    vector<int> result=eat(5,6,10);
    cout<<result[0]<<" "<<result[1]<<endl;
    result=eat(4