    vector<int> result(game.size());
    for(int i=0; i<game.size(); i++){
        result[i] = abs(game[i] - guess[i]);
    }
    return result;
}

int main()
{
    vector<int> game{1,2,3,4,5,1};
    vector<int> guess{1,2,3,4,2,-2};
    vector<int> result = compare(game,guess);
    for (int i=0; i<result.size(); i++)
       printf("%d ", result[i]);
    return 0;
}
*/

//Programming/C++/CodingTests/test1.cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> compare(vector<int> game, vector<int> guess) {
    vector<int> result(game.size());
    for (int i = 0; i < game.size(); i++) {
        result[i] = abs(game[i] - guess[i]);
    }
    return result;
}

int main() {
    vector<int> game{1, 2, 3, 4, 5, 1};
    vector<int> guess{1, 2, 3, 4, 2, -2};
    vector<int> result = compare(game, guess);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}

//Programming/C++/CodingTests/test2.cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> compare(vector<int> game, vector<int> guess) {
    vector<int> result(game.size());
    for (int i = 0; i < game.size(); i++) {
        result[i] = abs(game[i] - guess[i]);
    }
    return result;