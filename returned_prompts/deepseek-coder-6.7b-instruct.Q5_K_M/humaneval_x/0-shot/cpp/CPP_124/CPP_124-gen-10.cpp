    if (date.size() != 10)
        return false;

    if (date[2] != '-' || date[5] != '-')
        return false;

    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    int m = stoi(month);
    int d = stoi(day);
    int y = stoi(year);

    if (m < 1 || m > 12)
        return false;

    if (d < 1 || d > 31)
        return false;

    if (m == 4 || m == 6 || m == 9 || m == 11){
        if(d > 30)
            return false;
    }

    if (m == 2){
        if (y % 400 == 0 || (y % 100 != 0 && y % 4 == 0)){
            if (d > 29)
                return false;
        }
        else{
            if (d > 28)
                return false;
        }
    }

    return true;
}
int main(){
    printf("%d", valid_date("03-11-2000"));
    printf("%d", valid_date("15-01-2012"));
    printf("%d", valid_date("04-0-2040"));
    printf("%d", valid_date("06-04-2020"));
    printf("%d", valid_date("06/04/2020"));
    return 0;
}
/*
Output:
1
0
0
1
0
*/

*/

//Exercise-1/main.cpp
#include <iostream>
#include "exercise.cpp"
using namespace std;

int main() {
    cout<<valid_date("03-11-2000")<<endl;
    cout<<valid_date("15-01-2012")<<endl;
    cout<<