    int a=s.find('a');
    int apples=stoi(s.substr(0,a-1));
    int o=s.find('o');
    int oranges=stoi(s.substr(a+13,o-a-13));
    return n-apples-oranges;
}

int main(){
    printf("%d\n",fruit_distribution("5 apples and 6 oranges", 19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n",fruit_distribution("2 apples and 3 oranges", 100));
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120));
    return 0;
}
*/

#include<iostream>
#include<string>
using namespace std;

int fruit_distribution(string s, int total_fruits){
    int apples_start = s.find('a');
    int apples_end = s.find(' ', apples_start);
    int apples = stoi(s.substr(apples_start + 6, apples_end - apples_start - 6));

    int oranges_start = s.find('o', apples_end);
    int oranges_end = s.find(' ', oranges_start);
    int oranges = stoi(s.substr(oranges_start + 7, oranges_end - oranges_start - 7));

    int mangoes = total_fruits - (apples + oranges);
    return mangoes;
}

int main(){
    cout << fruit_distribution("5 apples and 6 oranges", 19) << endl;
    cout << fruit_distribution("0 apples and 1 oranges", 3) << endl;
    cout << fruit_distribution("2 apples and 3 oranges", 100) << endl;
    cout << fruit_distribution("100 apples and 1 oranges", 120) << endl;
    return 0;
}
*/

/*
//