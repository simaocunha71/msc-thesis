string new_str = "";

    for(int i = 0; i < str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            new_str += (char)(str[i] - 32); // subtract 32 to convert lowercase to uppercase
        }
        else if(str[i] >= 'A' && str[i] <= 'Z'){
            new_str += (char)(str[i] + 32); // add 32 to convert uppercase to lowercase
        }
        else{
            new_str += str[i]; // if not alphabet, keep it as it is
        }
    }
    return new_str;
}

int main(){
    string str = "Hello";
    string new_str = filp_case(str);
    cout << new_str << endl;  // output: "hELLO"
    return 0;
}  // Output: hELLO

Here's the explanation:

We create a new string `new_str` and iterate through each character of the original string `str`. For each character, we check if it's a lowercase letter (using the ASCII values). If it is, we subtract 32 from its ASCII value to convert it to uppercase. If it's an uppercase letter, we add 32 to convert it to lowercase. If the character is not a letter (e.g., a digit or punctuation mark), we simply add it to `new_str` as is.

The `filp_case` function returns the modified string `new_str`. In the `main` function, we call `filp_case` with the string "Hello" and print the result, which is "hELLO". 