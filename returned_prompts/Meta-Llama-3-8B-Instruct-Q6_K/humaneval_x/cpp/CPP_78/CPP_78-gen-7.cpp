    int count = 0;
    for(int i = 0; i < num.length(); i++){
        char c = num[i];
        if(c == 'A' || c == 'B' || c == 'C' || c == 'D' || c == 'E' || c == 'F'){
            if(c == 'B' || c == 'D' || c == 'F'){
                count++;
            }
        }
        else{
            int d = c - '0';
            if(d == 2 || d == 3 || d == 5 || d == 7){
                count++;
            }
        }
    }
    return count;
}

int main()
{
    string num = "ABED1A33";
    printf("%d", hex_key(num));
    return 0;
}

B:
    int hex_key(string num){
        int count = 0;
        for(int i = 0; i < num.length(); i++){
            char c = num[i];
            if(c >= 'A' && c <= 'F'){
                if(c == 'B' || c == 'D' || c == 'F'){
                    count++;
                }
            }
            else{
                int d = c - '0';
                if(d == 2 || d == 3 || d == 5 || d == 7){
                    count++;
                }
            }
        }
        return count;
    }
    int main()
    {
        string num = "ABED1A33";
        printf("%d", hex_key(num));
        return 0;
    }

C:
    int hex_key(string num){
        int count = 0;
        for(int i = 0; i < num.length(); i++){
            char c = num[i];
            if(c >= '2' && c <= '9'){
                if(c == '2' || c == '3' || c == '5' || c == '7'){
                    count++;
                }
            }
            else if(c >= 'A' && c <= 'F'){
                if(c == 'B' || c == 'D' || c == 'F'){
                    count++;
                }
            }
        }
        return count;
    }
    int main()
    {
        string num = "ABED1A33";
        printf("%d", hex_key(num));
        return 0;
    }

D:
    int hex_key(string num){
        int count = 0;
        for(int