    int ret = 0;
    int i = 0;
    int j = 0;
    int k = 0;
    int l = 0;
    int m = 0;
    while(num[i] != '\0'){
        if(num[i] == '0' || num[i] == '1' || num[i] == '2' || num[i] == '3' || num[i] == '4' || num[i] == '5' || num[i] == '6' || num[i] == '7' || num[i] == '8' || num[i] == '9'){
            k = num[i] - '0';
            m = 0;
            while(k > 0){
                m = m*10 + k%10;
                k = k/10;
            }
            if(m == 1 || m == 2 || m == 3 || m == 5 || m == 7 || m == 11 || m == 13 || m == 17 || m == 19){
                ret++;
            }
        }else if(num[i] == 'A' || num[i] == 'B' || num[i] == 'C' || num[i] == 'D' || num[i] == 'E' || num[i] == 'F'){
            j = num[i] - 'A' + 10;
            if(j == 2 || j == 3 || j == 5 || j == 7 || j == 11 || j == 13 || j == 17 || j == 19){
                ret++;
            }
        }
        i++;
    }
    return ret;
}
int main(){

    char num[100];
    scanf("%s",num);
    printf("%d\n",hex_key(num));
}

*/
















































