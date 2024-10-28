    if (n == 1)
        return "0";
    else{
        string temp;
        temp = string_sequence(n-1);
        temp.append(" ").append(to_string(n-1));
        return temp;
    }
}

int main(){
    printf("%s\n", string_sequence(5));
    return 0;
}