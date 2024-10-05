    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        result.push_back(abs(game[i] - guess[i] ));
    }
    return result;
}

int main(){
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> res = compare(game,guess);
    for(int i=0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

//This program will output: 0 0 0 0 3 3
*/

*/

#include<iostream>
#include<math.h>
#include<vector>
using namespace std;

vector<int> compare(vector<int> game,vector<int> guess){
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        result.push_back(abs(game[i] - guess[i] ));
    }
    return result;
}

int main(){
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> res = compare(game,guess);
    for(int i=0; i < res.size(); i++)
        cout << res[i] << " ";
    return 0;
}
//This program will output: 0 0 0 0 3 3
*/

*/

//The solution is in C++ and it is a function that takes two vectors as arguments. 
//The function iterates over both vectors simultaneously and for each pair of elements, it calculates the absolute difference between them. 
//It then pushes this difference into a new vector which it returns. 
//This new vector has the same length as the input vectors and contains the differences between the corresponding elements of the input vectors.
//If the guesses were correct, the differences will be