    for(int i=0;i<game.size();i++){
        if(guess[i]==game[i]){
            guess[i]=0;
        }
        else{
            guess[i]=abs(guess[i]-game[i]);
        }
    }
    return guess;
}

int main(){
    vector<int> game,guess;
    vector<int> result;
    int size;
    printf("enter the size of array:\n");
    scanf("%d",&size);
    printf("enter the game array:\n");
    for(int i=0;i<size;i++){
        scanf("%d",&game[i]);
    }
    printf("enter the guess array:\n");
    for(int i=0;i<size;i++){
        scanf("%d",&guess[i]);
    }
    result=compare(game,guess);
    for(int i=0;i<size;i++){
        printf("%d ",result[i]);
    }
    return 0;
}


