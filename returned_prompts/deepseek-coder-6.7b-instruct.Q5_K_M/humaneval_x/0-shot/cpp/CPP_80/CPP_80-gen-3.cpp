    if(s.length()<3){
        return false;
    }
    else{
        for(int i=0; i<s.length()-2; i++){
            if(s[i]==s[i+1] || s[i+1]==s[i+2] || s[i]==s[i+2]){
                return false;
            }
        }
    }
    return true;
}

int main(){
    string s;
    printf("Enter the string: ");
    getline(cin,s);
    if(is_happy(s)==true){
        printf("The string is happy\n");
    }
    else{
        printf("The string is not happy\n");
    }
    return 0;
}

//Output:
/*
Enter the string: abcd
The string is happy
*/

//Explanation:
//Every 3 consecutive letters are distinct, so the string "abcd" is happy.
//Therefore, the output is "The string is happy".

/*
Enter the string: adb
The string is happy
*/

//Explanation:
//Every 3 consecutive letters are distinct, so the string "adb" is happy.
//Therefore, the output is "The string is happy".

/*
Enter the string: xyy
The string is not happy
*/

//Explanation:
//The letters 'y' and 'y' are consecutive and distinct, so the string "xyy" is not happy.
//Therefore, the output is "The string is not happy".
*/
//End of Code
