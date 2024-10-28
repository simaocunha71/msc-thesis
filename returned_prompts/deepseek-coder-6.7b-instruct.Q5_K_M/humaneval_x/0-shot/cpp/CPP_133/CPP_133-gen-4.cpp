    int sum=0;
    for(int i=0;i<lst.size();i++){
        sum+=ceil(lst[i])*ceil(lst[i]);
    }
    return sum;
}

int main() {
    vector<float> lst = {1.4,4.2,0};
    printf("%d\n", sum_squares(lst));
    return 0;
}


*/

#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

int sum_squares(vector<float> lst){
    int sum=0;
    for(int i=0;i<lst.size();i++){
        sum+=ceil(lst[i])*ceil(lst[i]);
    }
    return sum;
}

int main() {
    vector<float> lst = {1.4,4.2,0};
    printf("%d\n", sum_squares(lst));
    return 0;
}

/*
In this code, we first declare a variable sum to keep track of the sum of the squares.
We then loop over all elements in the given vector lst, round each element to the upper integer using the ceil function, square the result, and add it to sum.
Finally, we return the sum.

The main function tests this with the vector lst = {1.4, 4.2, 0}. The function should return 29.
*/


/*
