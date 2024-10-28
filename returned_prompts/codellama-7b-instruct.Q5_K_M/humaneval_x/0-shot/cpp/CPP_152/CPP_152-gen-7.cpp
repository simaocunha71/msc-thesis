    vector<int> res;
    for(int i=0;i<game.size();i++){
        if(guess[i]==game[i])
            res.push_back(0);
        else
            res.push_back(abs(guess[i]-game[i]));
    }
    return res;
}

int main()
{
    vector<int> a={1,2,3,4,5,1};
    vector<int> b={1,2,3,4,2,-2};
    vector<int> res=compare(a,b);
    for(int i=0;i<res.size();i++){
        printf("%d ",res[i]);
    }
    printf("\n");
    return 0;
}
