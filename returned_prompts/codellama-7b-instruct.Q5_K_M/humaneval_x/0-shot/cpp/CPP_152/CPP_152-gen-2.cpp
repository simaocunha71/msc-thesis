    vector<int> result;
    for(int i=0;i<game.size();i++){
        if(abs(game[i]-guess[i])==0){
            result.push_back(0);
        }
        else{
            result.push_back(abs(game[i]-guess[i]));
        }
    }
    return result;
}

int main(){
    vector<int> game={1,2,3,4,5,1};
    vector<int> guess={1,2,3,4,2,-2};
    vector<int> res=compare(game,guess);
    for(int i=0;i<res.size();i++){
        printf("%d ",res[i]);
    }
    return 0;
}


