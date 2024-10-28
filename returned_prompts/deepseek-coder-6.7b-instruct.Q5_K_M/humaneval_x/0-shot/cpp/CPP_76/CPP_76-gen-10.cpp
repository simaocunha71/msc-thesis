    int result = 1;
    for(int i = 1; i <= x; i++){
        result *= n;
        if(result == x)
            return true;
        if(result > x)
            return false;
    }
    return false;
}

int main(){
    printf("%d\n", is_simple_power(1, 4)); //1
    printf("%d\n", is_simple_power(2, 2)); //1
    printf("%d\n", is_simple_power(8, 2)); //1
    printf("%d\n", is_simple_power(3, 2)); //0
    printf("%d\n", is_simple_power(3, 1)); //0
    printf("%d\n", is_simple_power(5, 3)); //0
    return 0;
}
*/

#include<iostream>
using namespace std;

bool is_simple_power(int x,int n){

    int result = 1;
    for(int i = 1; i <= x; i++){
        result *= n;
        if(result == x)
            return true;
        if(result > x)
            return false;
    }
    return false;
}

int main(){
    cout<<is_simple_power(1, 4)<<endl; //1
    cout<<is_simple_power(2, 2)<<endl; //1
    cout<<is_simple_power(8, 2)<<endl; //1
    cout<<is_simple_power(3, 2)<<endl; //0
    cout<<is_simple_power(3, 1)<<endl; //0
    cout<<is_simple_power(5, 3)<<endl; //0
    return 0;
}

//output: 
//1
//1
//1
//0
//0
//0
//Process returned 0 (0x0)   execution time : 0.002 s
//Press any key to continue.
//
//
//
//
//
//
//
//
