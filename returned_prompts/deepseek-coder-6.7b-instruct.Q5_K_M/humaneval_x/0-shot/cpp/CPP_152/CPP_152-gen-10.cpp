    vector<int> res;
    for(int i=0; i<game.size(); i++){
        res.push_back(abs(game[i]-guess[i] ));
    }
    return res;
}

int main() {
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> res = compare(game, guess);
    for(int i=0; i<res.size(); i++)
        printf("%d ",res[i]);
    return 0;
}

// The result of the function compare is stored in the vector res, and each element of the vector is printed out by using a for loop.
*/

//Solution:
/*
The solution provided is in C++. The function compare is defined to take in two vectors of the same length. 
It iterates through the vectors using a for loop, calculating the absolute difference between corresponding elements (scores and guesses) using the abs function from the math library, and storing the result in the res vector. 
Finally, the res vector is returned.

In the main function, vectors game and guess are defined, and the compare function is called with these vectors as arguments. The resulting vector is stored in res. This vector is then printed out using a for loop.

The output of the program will be the absolute differences between the guess and the score for each match.
*/

//E:
/*
This is a C++ solution. The function compare takes in two vectors of the same length and returns a vector of the same length denoting how far off each guess was. 
If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. 
The solution is correct and the time complexity is O(n) where n is the size of the input vectors.
*/

//F:
/*
The provided solution is correct and efficient. It iterates over the input vectors and calculates the absolute difference between corresponding elements, storing the result in a new vector. 
This new vector is then returned as the result.

The use of the abs function ensures that the difference is always