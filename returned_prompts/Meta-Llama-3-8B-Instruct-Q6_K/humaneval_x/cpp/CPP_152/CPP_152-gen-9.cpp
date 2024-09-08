    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }else{
            result.push_back(abs(game[i] - guess[i]));
        }
    }
    return result;
}
B:
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        result.push_back(game[i] - guess[i]);
    }
    for(int i = 0; i < result.size(); i++){
        if(result[i] == 0){
            result[i] = 0;
        }else{
            result[i] = abs(result[i]);
        }
    }
    return result;
}
C:
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        result.push_back(abs(game[i]-guess[i]));
    }
    return result;
}
D:
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }else{
            result.push_back(abs(game[i]-guess[i]));
            result.push_back(abs(game[i]-guess[i]));
        }
    }
    return result;
}
E:
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }else{
            result.push_back(game[i]-guess[i]);
        }
    }
    for(int i = 0; i < result.size(); i++){
        if(result[i] < 0){
            result[i] = -result[i];
        }
    }
    return result;
}
F:
    vector<int> result;
    for(int i = 0; i < game.size(); i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }else{
            result.push_back(abs(game[i]-guess[i]));
        }
    }
    return result;
}

int main(){
    // test cases
    vector<int> game1 = {1,2,3,4,5,1};
    vector<int> guess1 = {1,2,3,4,2,-2};
    vector<int> result1 = compare(game1,guess1);
    for(int i = 0; i < result1.size(); i++){
        printf("%d ",