    for(int i=n-1; i>0; i--){
        if(n%i==0)
            return i;
    }
}

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Largest divisor is: %d", largest_divisor(num));
    return 0;
}
*/
#include <iostream>
using namespace std;

int largest_divisor(int n){
    for(int i=n-1; i>0; i--){
        if(n%i==0)
            return i;
    }
}

int main(){
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    cout<<"Largest divisor is: "<<largest_divisor(num);
    return 0;
}

//C++/Assignment_4/q3.cpp
//