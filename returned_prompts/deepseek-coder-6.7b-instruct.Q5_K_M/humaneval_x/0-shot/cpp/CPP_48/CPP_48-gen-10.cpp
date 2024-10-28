    int length = text.size();
    for(int i = 0; i < length/2; i++){
        if(text[i] != text[length - 1 - i]){
            return false;
        }
    }
    return true;
}

int main(){
    printf("%d", is_palindrome("aba"));
    return 0;
}

The code above checks if a string is a palindrome. It takes a string, calculates its length, and then compares the first and last character, second and second last character and so on. If the characters are not the same, it returns false (not a palindrome). If all pairs of characters are the same, it returns true (a palindrome). The function is case sensitive, meaning it treats uppercase and lowercase characters as different.
*/

/*
