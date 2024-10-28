    int odd_lst1 = 0;
    int odd_lst2 = 0;
    for(int i=0; i<lst1.size(); i++){
        if(lst1[i]%2 != 0)
            odd_lst1++;
        if(lst2[i]%2 != 0)
            odd_lst2++;
    }
    if(odd_lst1 <= odd_lst2)
        return "YES";
    else
        return "NO";

This function will count the number of odd numbers in lst1 and lst2. If the number of odd numbers in lst1 is less than or equal to the number of odd numbers in lst2, then it is possible to exchange elements to make lst1 all even, so it will return "YES". Otherwise, it is impossible, so it will return "NO".

*/

//Code by Cpp

#include <iostream>
#include <vector>
#include <string>

std::string exchange(std::vector<int> lst1, std::vector<int> lst2) {
    int odd_lst1 = 0;
    int odd_lst2 = 0;
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i] % 2 != 0)
            odd_lst1++;
        if(lst2[i] % 2 != 0)
            odd_lst2++;
    }
    if(odd_lst1 <= odd_lst2)
        return "YES";
    else
        return "NO";
}

int main() {
    std::vector<int> lst1 = {1, 2, 3, 4