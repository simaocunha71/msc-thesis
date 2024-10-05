    for(int i=n-1; i>0; i--){
        if(n%i == 0){
            return i;
        }
    }

}
int main(){
    int n;
    scanf("%d", &n);
    printf("%d", largest_divisor(n));
    return 0;
}

#include<iostream>
using namespace std;
int largest_divisor(int n){

    for(int i=n-1; i>0; i--){
        if(n%i == 0){
            return i;
        }
    }

}
int main(){
    int n;
    cin >> n;
    cout << largest_divisor(n);
    return 0;
}

*/

#include<iostream>
using namespace std;
int largest_divisor(int n){

    for(int i=n-1; i>0; i--){
        if(n%i == 0){
            return i;
        }
    }

}
int main(){
    int n;
    cin >> n;
    cout << largest_divisor(n);
    return 0;
}

//Test Case:
//input: 15
//output: 5
//Explanation: The largest integer that divides 15 evenly is 5.

//Test Case:
//input: 20
//output: 5
//Explanation: The largest integer that divides 20 evenly is 5.

//Test Case:
//input: 1
//output: 1
//Explanation: 1 is not a valid number to divide by, because dividing by 1 does not give a remainder.
//So, the largest divisor of 1 is itself.

//Test Case:
//input: 100
//output: 5
//Explanation: The largest integer that divides 100 evenly is 5.

//Test Case:
//input: 1000
//output: 5
//Explanation: The largest integer that divides 1000 evenly is 5