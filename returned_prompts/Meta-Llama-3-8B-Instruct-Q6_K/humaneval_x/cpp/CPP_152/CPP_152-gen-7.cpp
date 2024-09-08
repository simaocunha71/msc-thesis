    vector<int> result;
    for(int i=0; i<game.size(); i++){
        int diff = abs(guess[i] - game[i]);
        result.push_back(diff);
    }
    return result;
}
int main() {
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> result = compare(game,guess);
    for(int i = 0; i < result.size(); i++){
        printf("%d ",result[i]);
    }
    printf("\n");
    return 0;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<int> compare(vector<int> scores, vector<int> guesses) {
    vector<int> result;
    for(int i = 0; i < scores.size(); i++) {
        if(scores[i] == guesses[i]) {
            result.push_back(0);
        } else {
            result.push_back(abs(scores[i] - guesses[i]));
        }
    }
    return result;
}

int main() {
    vector<int> scores = {1,2,3,4,5,1};
    vector<int> guesses = {1,2,3,4,2,-2};
    vector<int> result = compare(scores, guesses);
    for(int i = 0; i < result.size(); i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
C:
#include <iostream>
#include <vector>

using namespace std;

vector<int> compare(vector<int> scores, vector<int> guesses) {
    vector<int> result;
    for(int i = 0; i < scores.size(); i++) {
        if(scores[i] == guesses[i]) {
            result.push_back(0);
        } else {
            result.push_back(abs(scores[i] - guesses[i]));
        }
    }
    return result;
}

int main() {
    vector<int> scores = {1,2,3,4,5,1};
    vector<int> guesses = {1,2,3,4,2,-2};
    vector<int> result = compare(scores, guesses);
    for(int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
D:
#include <iostream>
#include