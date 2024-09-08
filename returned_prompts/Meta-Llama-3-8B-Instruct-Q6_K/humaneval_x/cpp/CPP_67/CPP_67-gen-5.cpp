    int start = s.find("apples");
    int end = s.find("oranges");
    int apples = 0, oranges = 0;
    if(start != -1 && end != -1){
        string apples_str = s.substr(start + 7, end - start - 7);
        apples = stoi(apples_str);
        string oranges_str = s.substr(end + 8);
        oranges = stoi(oranges_str);
    }
    else if(start != -1){
        string apples_str = s.substr(start + 7);
        apples = stoi(apples_str);
    }
    else if(end != -1){
        string oranges_str = s.substr(end + 8);
        oranges = stoi(oranges_str);
    }
    else{
        apples = oranges = 0;
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
B:
    int fruit_distribution(string s, int n) {
        int mangoes = n;
        string str = s;
        size_t found = str.find("apples");
        if (found != string::npos) {
            size_t found2 = str.find("oranges");
            string apple_str = str.substr(found + 7, found2 - found - 7);
            int apples = stoi(apple_str);
            string orange_str = str.substr(found2 + 8);
            int oranges = stoi(orange_str);
            mangoes = n - apples - oranges;
        }
        return mangoes;
    }
    int main() {
        printf("%d\n", fruit_distribution("5 apples and 6 oranges", 19));
        printf("%d\n", fruit_distribution("0 apples and 1 oranges", 3));
        printf("%d\n", fruit_distribution("2 apples and 3 oranges", 100));
        printf("%d\n", fruit_distribution("100 apples and 1 oranges", 120));
        return 0;
    }
C:
    int fruit_distribution(string s, int n) {
        int mangoes = n;
        size_t found = s.find("apples");
        if (found