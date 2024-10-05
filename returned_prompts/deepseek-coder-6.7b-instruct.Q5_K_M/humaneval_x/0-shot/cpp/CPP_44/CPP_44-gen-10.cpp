    string converted = "";
    int remainder;

    while(x != 0){
        remainder = x % base;
        x = x / base;
        converted = to_string(remainder) + converted;
    }

    return converted;
}

int main(){
    int x, base;
    scanf("%d %d", &x, &base);
    string converted = change_base(x, base);
    printf("%s", converted.c_str());
    return 0;
}
*/


