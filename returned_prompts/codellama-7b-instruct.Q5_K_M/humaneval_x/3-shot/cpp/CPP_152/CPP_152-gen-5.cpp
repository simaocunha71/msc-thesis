    vector<int> results;
    int score;
    int guess_score;
    int i;
    for (i=0;i<game.size();i++){
        score=game[i];
        guess_score=guess[i];
        if (score==guess_score)
        results.push_back(0);
        else
        results.push_back(abs(guess_score-score));
    }
    return results;
}


