    for(int i=0;str[i] != '\0'; i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = str[i] - 32;
        }
        else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] = str[i] + 32;
        }
    }
    return str;
}

int main(){
    string str;
    cout<<"Enter a string: ";
    cin>>str;
    str = filp_case(str);
    cout<<"Flipped case string: "<<str;
    return 0;
}

Output:
Enter a string: Hello
Flipped case string: hELLO

*/

