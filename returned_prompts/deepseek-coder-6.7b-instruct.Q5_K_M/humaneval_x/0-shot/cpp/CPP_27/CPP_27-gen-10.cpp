    for (int i = 0; str[i]; i++) {
        if (str[i] >= 'a' && str[i] <= 'z')
            str[i] = str[i] - 32;
        else if (str[i] >= 'A' && str[i] <= 'Z')
            str[i] = str[i] + 32;
    }
    return str;
}
int main(){
    string str;
    printf("Enter a string: ");
    getline(cin,str);
    printf("Flipped case string: %s", filp_case(str).c_str());
    return 0;
}

