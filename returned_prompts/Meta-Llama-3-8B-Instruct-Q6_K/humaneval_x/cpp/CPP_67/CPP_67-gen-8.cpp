    int total_apples = 0;
    int total_oranges = 0;
    int start = 0;
    int end = s.length();
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' && s[i+1] == 'p'){
            start = i + 4;
            while(s[i] != 's' && i < end){
                if(s[i] >= '0' && s[i] <= '9'){
                    total_apples = total_apples * 10 + (s[i] - '0');
                }
                i++;
            }
        }
        if(s[i] == 'o' && s[i+1] == 'r'){
            start = i + 6;
            while(s[i] != 's' && i < end){
                if(s[i] >= '0' && s[i] <= '9'){
                    total_oranges = total_oranges * 10 + (s[i] - '0');
                }
                i++;
            }
        }
    }
    return n - total_apples - total_oranges;
}
int main(){
    printf("%d\n",fruit_distribution("5 apples and 6 oranges", 19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n",fruit_distribution("2 apples and 3 oranges", 100));
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120));
    return 0;
}
B:
    The function `fruit_distribution` takes a string `s` and an integer `n` as input. 
    It parses the string `s` to extract the number of apples and oranges, and then 
    returns the difference between `n` and the sum of the number of apples and oranges.
    The function uses a loop to iterate over the string `s` and checks if each character 
    is a letter or a digit. If a character is a letter, it checks if it is the start of 
    the word "apples" or "oranges". If it is, it extracts the number of apples or oranges 
    from the string and adds it to the corresponding variable.
    Finally, the function returns the difference between `n` and the sum of the number 
    of apples and oranges.

C:
    The function `fruit_distribution` takes a string `s` and an integer `n` as input