    vector<int> result;
    for(int i=0; i<game.size(); i++)
        result.push_back(abs(game[i]-guess[i] ));
    return result;
}

int main(){
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> result = compare(game,guess);
    for(int i=0;i<result.size();i++)
        printf("%d ",result[i]);
    return 0;
}

*/

*/

