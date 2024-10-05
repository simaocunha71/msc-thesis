
    vector<int> result;
    for(int i=0; i<game.size(); i++)
        result.push_back(abs(game[i]-guess[i] ));
    return result;
}
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

vector<int> compare(vector<int> game, vector<int> guess) {
    
    vector<int> result;
    for(int i = 0; i < game.size(); i++)
        result.push_back(abs(game[i] - guess[i]));
    return result;
}

int main()
{
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> result = compare(game, guess);
    
    printf("[");
    for (int i = 0; i < result.size(); i++) {
        printf("%d", result[i]);
        if(i < result.size() - 1)
            printf(", ");
    }
    printf("]\n");
    
    return 0;
}
```

The `compare()` function is defined to take two vectors as arguments. It calculates the absolute difference between the corresponding elements of the two vectors, and stores these differences in a new vector. This new vector is then returned. The `main()` function demonstrates usage of the `compare()` function by passing two vectors to it and printing the result.




























































































































