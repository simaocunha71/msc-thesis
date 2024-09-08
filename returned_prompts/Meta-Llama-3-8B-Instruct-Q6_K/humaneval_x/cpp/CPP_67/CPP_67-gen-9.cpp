    int count = 0;
    string word = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] == ' '){
            if(word == "apples" || word == "oranges"){
                int num = stoi(word);
                count += num;
            }
            word = "";
        }else{
            word += s[i];
        }
    }
    if(word == "apples" || word == "oranges"){
        int num = stoi(word);
        count += num;
    }
    return n - count;

}int main(){
    printf("%d\n",fruit_distribution("5 apples and 6 oranges",19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n",fruit_distribution("2 apples and 3 oranges",100));
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120));
    return 0;
} 
