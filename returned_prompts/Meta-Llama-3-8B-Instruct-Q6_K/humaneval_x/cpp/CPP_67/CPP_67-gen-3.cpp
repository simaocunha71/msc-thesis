    int count = 0;
    int i = 0;
    while(i < s.length()){
        if(s[i] == ' '){
            i++;
            continue;
        }
        if(s[i] == 'a'){
            int j = i;
            while(j < s.length() && s[j] != ' '){
                j++;
            }
            int num_apples = stoi(s.substr(i,j-i));
            i = j+1;
            n = n - num_apples;
        }
        else if(s[i] == 'o'){
            int j = i;
            while(j < s.length() && s[j] != ' '){
                j++;
            }
            int num_oranges = stoi(s.substr(i,j-i));
            i = j+1;
            n = n - num_oranges;
        }
        else{
            i++;
        }
    }
    return n;

}
int main(){
    string s;
    int n;
    printf("Enter a string that represents the total number of the oranges and apples: ");
    getline(cin,s);
    printf("Enter the total number of the fruits in the basket: ");
    scanf("%d",&n);
    printf("The number of the mango fruits in the basket is: %d\n",fruit_distribution(s,n));
    return 0;
}
