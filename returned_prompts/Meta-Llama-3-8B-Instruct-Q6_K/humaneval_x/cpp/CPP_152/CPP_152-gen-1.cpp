    vector<int> result;
    for(int i=0;i<game.size();i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }
        else{
            result.push_back(abs(game[i]-guess[i]));
        }
    }
    return result;
}

int main(){
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> result = compare(game,guess);
    for(auto i : result){
        printf("%d ",i);
    }
    printf("\n");
    return 0;
}

B:
    vector<int> compare(vector<int> game, vector<int> guess) {
        vector<int> result;
        for (int i = 0; i < game.size(); i++) {
            result.push_back(abs(game[i] - guess[i]));
        }
        return result;
    }

    int main() {
        vector<int> game = {1, 2, 3, 4, 5, 1};
        vector<int> guess = {1, 2, 3, 4, 2, -2};
        vector<int> result = compare(game, guess);
        for (auto i : result) {
            printf("%d ", i);
        }
        printf("\n");
        return 0;
    }
C:
    #include <iostream>
    #include <vector>
    #include <algorithm>

    std::vector<int> compare(std::vector<int> game, std::vector<int> guess) {
        std::vector<int> result;
        for (int i = 0; i < game.size(); i++) {
            if (game[i] == guess[i]) {
                result.push_back(0);
            } else {
                result.push_back(std::abs(game[i] - guess[i]));
            }
        }
        return result;
    }

    int main() {
        std::vector<int> game = {1, 2, 3, 4, 5, 1};
        std::vector<int> guess = {1, 2, 3, 4, 2, -2};
        std::vector<int> result = compare(game, guess);
        for (auto i : result) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
        return 0;
   