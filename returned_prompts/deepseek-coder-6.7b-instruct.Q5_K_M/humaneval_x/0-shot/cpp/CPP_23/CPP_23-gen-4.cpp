    int count=0;
    for(int i=0; str[i] != '\0'; i++)
        count++;
    return count;
}

int main(){
    string str;
    printf("Enter a string: ");
    getline(cin, str);
    printf("Length of string: %d", strlen(str));
    return 0;
}

