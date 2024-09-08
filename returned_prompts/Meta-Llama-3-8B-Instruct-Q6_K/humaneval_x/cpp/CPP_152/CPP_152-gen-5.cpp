    vector<int> res;
    int n = game.size();
    for(int i = 0; i < n; i++){
        res.push_back(abs(game[i]-guess[i]));
    }
    return res;
}

B:
    vector<int> res;
    int n = game.size();
    for(int i = 0; i < n; i++){
        if(game[i] == guess[i]) res.push_back(0);
        else res.push_back(abs(game[i]-guess[i]));
    }
    return res;
}

C:
    vector<int> res;
    int n = game.size();
    for(int i = 0; i < n; i++){
        res.push_back(game[i] == guess[i]?0:abs(game[i]-guess[i]));
    }
    return res;
}
int main() {
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> res = compare(game,guess);
    for(auto i : res) cout << i << " ";
    return 0;
}
}
output:
0 0 0 0 3 3
*/



Explanation:

This problem is asking to compare the results of a number of matches where we have two vectors, one for the actual scores and one for the guesses. The task is to calculate the difference between the actual scores and the guesses. If the guess is correct, the difference is 0, otherwise it's the absolute difference between the actual score and the guess.

There are three different ways to solve this problem, each with its own logic. 

In the first solution (A), we iterate through both vectors and calculate the absolute difference between the actual score and the guess. We then add this difference to the result vector.

In the second solution (B), we check if the actual score is equal to the guess. If it is, we add 0 to the result vector. Otherwise, we add the absolute difference between the actual score and the guess to the result vector.

In the third solution (C), we use a conditional operator to check if the actual score is equal to the guess. If it is, we return 0, otherwise we return the absolute difference between the actual score and the guess.

The output of the program will be a vector of the same length as the input vectors, where each element represents the difference between the actual score and the guess for that match. If