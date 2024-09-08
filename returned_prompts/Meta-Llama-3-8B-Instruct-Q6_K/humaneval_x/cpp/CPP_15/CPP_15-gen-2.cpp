    string result = "";
    for(int i = 0; i <= n; i++){
        result += to_string(i) + " ";
    }
    return result;
}

int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("%s\n", string_sequence(n).c_str());
    return 0;
}

