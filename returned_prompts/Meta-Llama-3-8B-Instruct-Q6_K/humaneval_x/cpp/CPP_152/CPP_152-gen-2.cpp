    vector<int> result;
    for(int i=0;i<game.size();i++){
        if(game[i]==guess[i]){
            result.push_back(0);
        }
        else{
            result.push_back(abs(game[i]-guess[i]));
        }
    }
    return result;
}

int main() {
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> result = compare(game,guess);
    for(int i=0;i<result.size();i++){
        printf("%d ",result[i]);
    }
    printf("\n");
    return 0;
}

B:
    #include <iostream>
    #include <vector>
    using namespace std;

    vector<int> compare(vector<int> scores, vector<int> guesses) {
        vector<int> results;
        for (int i = 0; i < scores.size(); i++) {
            if (scores[i] == guesses[i]) {
                results.push_back(0);
            } else {
                results.push_back(abs(scores[i] - guesses[i]));
            }
        }
        return results;
    }

    int main() {
        vector<int> scores = {1, 2, 3, 4, 5, 1};
        vector<int> guesses = {1, 2, 3, 4, 2, -2};
        vector<int> results = compare(scores, guesses);
        for (int i = 0; i < results.size(); i++) {
            cout << results[i] << " ";
        }
        cout << endl;
        return 0;
    }

C:
    public class Main {
        public static java.util.List<Integer> compare(java.util.List<Integer> game, java.util.List<Integer> guess) {
            java.util.List<Integer> result = new java.util.ArrayList<>();
            for (int i = 0; i < game.size(); i++) {
                if (game.get(i).equals(guess.get(i))) {
                    result.add(0);
                } else {
                    result.add(Math.abs(game.get(i) - guess.get(i)));
                }
            }
            return result;
        }

        public static void main(String[] args) {
            java.util.List<Integer> game = new java.util.ArrayList<>();
            game.add(1);
            game.add(2);
            game.add(3);
            game.add(4);
            game.add(5