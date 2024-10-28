#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){
    int odd1 = 0, even1 = 0, odd2 = 0, even2 = 0;
    for(int i=0; i<lst1.size(); i++){
        if(lst1[i] % 2 == 0)
            even1++;
        else
            odd1++;
    }

    for(int i=0; i<lst2.size(); i++){
        if(lst2[i] % 2 == 0)
            even2++;
        else
            odd2++;
    }

    if(even1 + odd2 >= odd1){
        return "YES";
    }
    else{
        return "NO";
    }
}
*/

//This solution works by counting the number of odd and even numbers in lst1 and lst2 respectively.
//If the number of odd numbers in lst1 plus the number of even numbers in lst2 is equal to or greater than the number of odd numbers in lst1,
//then it's possible to make all the numbers in lst1 even by exchanging elements between lst1 and lst2.
//If it's not possible, then it's impossible.

//This solution assumes that the input vectors are non-empty.
//If the input vectors could be empty, then additional checks would need to be added to handle this case.

//This solution has a time complexity of O(n) where n is the size of the input vectors.
//This is because it makes a single pass over each of the input vectors to count the number of odd and even numbers.

//This solution has a space complexity of O(1) because it only uses a constant number of variables to store the counts of odd and even numbers in the input vectors.
//This makes it more memory efficient than other solutions that might use additional data structures to store the counts.

//The solution is correct because it correctly determines whether it's possible to make all the numbers in lst1 even by exchanging elements between lst1 and lst2