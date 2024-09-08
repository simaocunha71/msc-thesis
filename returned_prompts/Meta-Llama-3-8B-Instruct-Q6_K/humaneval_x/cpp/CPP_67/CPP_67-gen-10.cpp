    int sum = 0;
    int apples = 0;
    int oranges = 0;
    string word = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' '){
            if(word == "apples"){
                apples = atoi(word.c_str());
            }
            else if(word == "oranges"){
                oranges = atoi(word.c_str());
            }
            word = "";
        }
        else if(s[i] != 'a' && s[i] != 'o' && s[i] != 'n' && s[i] != 'g' && s[i] != 'm' && s[i] != ' '){
            word += s[i];
        }
    }
    if(word == "apples"){
        apples = atoi(word.c_str());
    }
    else if(word == "oranges"){
        oranges = atoi(word.c_str());
    }
    return n - apples - oranges;
}
int main(){
    printf("%d\n",fruit_distribution("5 apples and 6 oranges",19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n",fruit_distribution("2 apples and 3 oranges",100));
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120));
    return 0;
}
