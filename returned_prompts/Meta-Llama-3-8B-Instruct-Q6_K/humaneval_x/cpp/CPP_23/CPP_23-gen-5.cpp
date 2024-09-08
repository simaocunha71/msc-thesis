    int count =0;
    for(int i=0; i<str.length(); i++){
        count++;
    }
    return count;

}int main(){
    string str;
    printf("Enter a string: ");
    getline(cin, str);
    printf("Length of the string is: %d\n", strlen(str));
    return 0;
}
}
