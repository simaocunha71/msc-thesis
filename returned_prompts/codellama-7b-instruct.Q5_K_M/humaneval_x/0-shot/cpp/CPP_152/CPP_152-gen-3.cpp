    vector<int> ans;
    for(int i=0;i<game.size();i++){
        if(game[i]==guess[i]){
            ans.push_back(0);
        }
        else{
            ans.push_back(abs(game[i]-guess[i]));
        }
    }
    return ans;
}

int main(){
    vector<int> game = {1,2,3,4,5,1};
    vector<int> guess = {1,2,3,4,2,-2};
    vector<int> ans = compare(game,guess);
    for(auto i:ans){
        printf("%d ",i);
    }
}

