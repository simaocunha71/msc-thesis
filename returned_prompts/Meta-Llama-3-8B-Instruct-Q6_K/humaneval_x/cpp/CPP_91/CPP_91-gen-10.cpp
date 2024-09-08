    int boredom_count=0;
    int i=0;
    while(i<S.length()){
        if(S[i]=='.' || S[i]=='?' || S[i]=='!'){
            //check if the sentence starts with "I"
            if(i>0 && S.substr(1,i-1).compare("I")==0){
                boredom_count++;
            }
            i++;
            //reset i to check the next sentence
            i++;
        }else{
            i++;
        }
    }
    return boredom_count;
}

int main()
{
    string s;
    printf("Enter a string: \n");
    getline(cin,s);
    printf("Number of boredoms: %d\n",is_bored(s));
    return 0;
}
