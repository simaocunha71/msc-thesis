    int apples=0,oranges=0;
    string temp="";
    for(int i=0;i<s.length();i++){
        if(s[i]==' ' || s[i]=='a' || s[i]=='n' || s[i]=='d'){
            if(temp=="apples"){
                apples=stoi(to_string(apples)+s[i]);
            }
            else if(temp=="oranges"){
                oranges=stoi(to_string(oranges)+s[i]);
            }
            temp="";
        }
        else{
            temp+=s[i];
        }
    }
    return n-apples-oranges;
}
int main(){
    printf("%d\n",fruit_distribution("5 apples and 6 oranges", 19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n",fruit_distribution("2 apples and 3 oranges", 100));
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120));
    return 0;
}

*/

// 3. Given a string of words, reverse the words in the string.
// Example:
// reverseWords("the sky is blue") -> "blue is sky the"

