    vector<int> diff;
    for(int i=0;i<game.size();i++){
        if(guess[i]==game[i]){
            diff.push_back(0);
        }else{
            diff.push_back(abs(guess[i]-game[i]));
        }
    }
    return diff;
}