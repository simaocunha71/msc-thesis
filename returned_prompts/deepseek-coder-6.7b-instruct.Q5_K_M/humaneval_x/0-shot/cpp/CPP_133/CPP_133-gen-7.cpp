    int sum = 0;
    for(int i=0; i<lst.size(); i++){
        sum += pow(ceil(lst[i]), 2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4, 4.2, 0};
    printf("%d\n", sum_squares(lst));
    return 0;
}


*/



// Answer:

/*

The task is to round each number in the given vector to the upper int(Ceiling) first, then calculate the square of each rounded number and sum them all up.

The function `sum_squares` takes a vector of floats as an argument.
It initializes a variable `sum` to 0.
Then it iterates over each number in the vector.
For each number, it calculates the ceiling using the `ceil` function and squares the result using the `pow` function.
It then adds the squared value to `sum`.
Finally, it returns `sum`.

In the `main` function, we call `sum_squares` with a vector `lst` containing the numbers 1.4, 4.2, and 0.
The result is printed to the console using `printf`.

*/

// Code:

#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int sum_squares(vector<float> lst){
    int sum = 0;
    for(int i=0; i<lst.size(); i++){
        sum += pow(ceil(lst[i]), 2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4, 4.2, 0};
    printf("%d\n", sum_squares(lst));
    return 0;
}

// Output:

// 29

// The numbers in the vector are rounded to 2 and 5 and 0 respectively, and their squares are added together, resulting in 29.

// Note: This code uses