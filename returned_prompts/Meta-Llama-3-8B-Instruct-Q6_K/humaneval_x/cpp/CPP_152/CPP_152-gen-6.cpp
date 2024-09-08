    vector<int> result;
    int i;
    for(i=0;i<game.size();i++){
        if(game[i] == guess[i]){
            result.push_back(0);
        }
        else{
            result.push_back(abs(game[i]-guess[i]));
        }
    }
    return result;
}
B:
    vector<int> result;
    for(int i=0; i<game.size(); i++){
        result.push_back(game[i] == guess[i] ? 0 : abs(game[i] - guess[i]));
    }
    return result;
}
C:
    vector<int> result;
    for(int i=0; i<game.size(); i++){
        result.push_back((game[i] == guess[i]? 0 : abs(game[i]-guess[i])));
    }
    return result;
}
D:
    vector<int> result;
    for(int i=0; i<game.size(); i++){
        result.push_back( game[i] == guess[i]? 0 : (game[i]-guess[i]) > 0 ? game[i]-guess[i] : -game[i]+guess[i]);
    }
    return result;
}
E:
    vector<int> result;
    for(int i=0; i<game.size(); i++){
        result.push_back((game[i] == guess[i]? 0 : (game[i] < guess[i] ?  game[i] - guess[i] : guess[i] - game[i])));
    }
    return result;

F:
    vector<int> result;
    for(int i=0; i<game.size(); i++){
        result.push_back((game[i] == guess[i]? 0 : (game[i] < guess[i] ?  abs(game[i] - guess[i]) : -abs(game[i] - guess[i]))));
    }
    return result;
}
G:
    vector<int> result;
    for(int i=0; i<game.size(); i++){
        result.push_back((game[i] == guess[i]? 0 : (game[i] < guess[i] ?  (game[i] - guess[i]) : -(guess[i] - game[i]))));
    }
    return result;

}
H:
    vector<int> result;
    for(int i=0; i<game.size(); i++){
        result.push_back((game[i] == guess[i]? 0 : (game[i] < guess[i] ?  abs(game[i] - guess[i]) : -abs(game[i] - guess[i