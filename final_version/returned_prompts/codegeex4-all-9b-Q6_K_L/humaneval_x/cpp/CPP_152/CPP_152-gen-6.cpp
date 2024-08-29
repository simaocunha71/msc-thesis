/*
1.  declare vector<int> result
2.  loop through game and guess
3.  compare each element
4.  if same, push 0 to result
5.  if different, push abs(guess - game) to result
6.  return result
*/
vector<int> compare(vector<int> game,vector<int> guess){
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }else{
            result.push_back(abs(guess[i] - game[i]));
        }
    }
    return result;
}

C:

1.  declare vector<int> result
2.  loop through game and guess
3.  compare each element
4.  if same, push 0 to result
5.  if different, push abs(guess - game) to result
6.  return result
*/

vector<int> compare(vector<int> game,vector<int> guess){
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }else{
            result.push_back(abs(guess[i] - game[i]));
        }
    }
    return result;
}

E:
/*
1.  declare vector<int> result
2.  loop through game and guess
3.  compare each element
4.  if same, push 0 to result
5.  if different, push abs(guess - game) to result
6.  return result
*/

vector<int> compare(vector<int> game,vector<int> guess){
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }else{
            result.push_back(abs(guess[i] - game[i]));
        }
    }
    return result;
}

F:
/*
1.  declare vector<int> result
2.  loop through game and guess
3.  compare each element
4.  if same, push 0 to result
5.  if different, push abs(guess - game) to result
6.  return result
*/

vector<int> compare(vector<int> game,vector<int> guess){
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i