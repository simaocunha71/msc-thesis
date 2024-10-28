    int odd_in_lst1 = 0;
    int odd_in_lst2 = 0;
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i] % 2 != 0)
            odd_in_lst1++;
    }
    for(int i = 0; i < lst2.size(); i++){
        if(lst2[i] % 2 != 0)
            odd_in_lst2++;
    }

    if(odd_in_lst1 > odd_in_lst2)
        return "NO";

B:
    int even_in_lst2 = lst2.size() - odd_in_lst2;
    if(odd_in_lst1 + even_in_lst2 < lst1.size())
        return "NO";

C:
    return "YES";
}

The function starts by counting the number of odd numbers in lst1 and lst2.
If the number of odd numbers in lst1 is greater than the number of odd numbers in lst2,
it is impossible to exchange elements to make all numbers in lst1 even. In this case, the function returns "NO".
The function then counts the number of even numbers in lst2.
If the sum of the number of odd numbers in lst1 and the number of even numbers in lst2 is less than the size of lst1,
it is also impossible to make all numbers in lst1 even. In this case, the function returns "NO".
If none of the above conditions are met, it is possible to exchange elements to make all numbers in lst1 even. In this case, the function returns "YES".
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){
    int odd_in_lst1 = 0;
    int odd_in_lst2 = 0;
    for(int i = 0; i < lst1.size(); i++){
        if(lst