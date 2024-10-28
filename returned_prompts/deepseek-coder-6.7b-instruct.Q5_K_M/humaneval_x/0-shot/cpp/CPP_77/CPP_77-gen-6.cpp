int temp;
temp=(int)cbrt(a);
if(a==temp*temp*temp)
return true;
else
return false;
}
int main()
{
    int a;
    printf("Enter the number:");
    scanf("%d",&a);
    if(iscuber(a))
    printf("True");
    else
    printf("False");
    return 0;
}

This program will take an integer as input and pass it to the function 'iscuber'. This function will then calculate the cubic root of the input integer, convert it to an integer and then cube it. If this result is equal to the original integer, the function will return true, otherwise it will return false. This result will then be printed out.

It uses the math library for the function cbrt, which calculates the cubic root of a number.
*/

// C++ code
#include<iostream>
#include<cmath>
using namespace std;

bool iscuber(int a){
    int temp;
    temp = cbrt(a);
    return (temp * temp * temp == a);
}

int main(){
    int a;
    cout << "Enter the number: ";
    cin >> a;
    if(iscuber(a))
        cout << "True";
    else
        cout << "False";
    return 0;
}

/*
