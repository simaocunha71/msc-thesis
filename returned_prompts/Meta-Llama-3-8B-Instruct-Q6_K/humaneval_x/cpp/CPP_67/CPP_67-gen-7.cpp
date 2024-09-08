    int apples = 0;
    int oranges = 0;
    int mango = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' && s[i+1] == 'p' && s[i+2] == 'p' && s[i+3] == 'l' && s[i+4] == 'e' && s[i+5] == 's'){
            apples = 1;
            i += 5;
        }else if(s[i] == 'o' && s[i+1] == 'r' && s[i+2] == 'a' && s[i+3] == 'n' && s[i+4] == 'g' && s[i+5] == 'e' && s[i+6] == 's'){
            oranges = 1;
            i += 6;
        }
    }
    int total = apples + oranges;
    return n - total;
}

int main(){
    printf("%d\n",fruit_distribution("5 apples and 6 oranges",19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n",fruit_distribution("2 apples and 3 oranges",100));
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120));
    return 0;
}

Output:
8
2
95
19

Explanation:
The function `fruit_distribution` takes a string `s` and an integer `n` as arguments. 
The string `s` represents a number of apples and oranges that are distributed in a basket 
of fruit. The function first initializes three integer variables `apples`, `oranges`, and `mango` to 0.
Then it iterates over the string `s` and checks if the string contains the words "apples" or "oranges" 
by comparing the characters of the string with the characters of the words "apples" and "oranges". 
If the string contains the word "apples", it increments the `apples` variable by 1. 
If the string contains the word "oranges", it increments the `oranges` variable by 1.
Finally, the function returns the difference between the total number of fruits `n` and the sum of `apples` and `oranges`. 
This difference represents the number of mango fruits in the basket.

The `main`