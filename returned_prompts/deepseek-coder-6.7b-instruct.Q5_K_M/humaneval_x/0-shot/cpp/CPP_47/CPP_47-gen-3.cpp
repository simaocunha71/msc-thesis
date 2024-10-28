    sort(l.begin(), l.end());
    int n = l.size();
    if(n % 2 == 0)
        return (l[n/2 - 1] + l[n/2]) / 2;
    else
        return l[n/2];
}
int main(){
    vector<float> v1 = {3, 1, 2, 4, 5};
    printf("%f\n", median(v1));
    vector<float> v2 = {-10, 4, 6, 1000, 10, 20};
    printf("%f\n", median(v2));
    return 0;
}

T:
/*
The function median takes a vector of float numbers as input and returns the median value of the vector.
It sorts the input vector in ascending order, then checks if the number of elements is even or odd.
If it's even, it returns the average of the two middle elements.
If it's odd, it returns the middle element.
*/

*/


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

float median(vector<float> l){
    sort(l.begin(), l.end());
    int n = l.size();
    if(n % 2 == 0)
        return (l[n/2 - 1] + l[n/2]) / 2;
    else
        return l[n/2];
}

int main(){
    vector<float> v1 = {3, 1, 2, 4, 5};
    cout<<median(v1)<<endl;
    vector<float> v2 = {-10, 4, 6, 1000, 10, 20};
    cout<<median(v2)<<endl;
    return 0;
}

*/



*/














































