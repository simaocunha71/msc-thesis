    int count = 0;
    bool check = false;
    for(int i = 0; i < S.size(); i++){
        if(S[i] == 'I'){
            check = true;
        }
        if(check && (S[i] == ' ' || i == S.size()-1)){
            if(i != S.size()-1 && S[i+1] != ' ')
                check = false;
            else
                count++;
        }
        if(S[i] == '.' || S[i] == '?' || S[i] == '!' || i == S.size()-1){
            check = false;
        }
    }
    return count;
}
int main(){
    printf("%d\n", is_bored("Hello world"));
    printf("%d\n", is_bored("The sky is blue. The sun is shining. I love this weather"));
    return 0;
}
*/

