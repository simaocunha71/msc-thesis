    if(n>m)
        return "-1";
    int sum=0;
    int count=(m-n+1);
    for(int i=n;i<=m;i++){
        sum+=i;
    }
    double avg = (double)sum / count;
    int int_avg = (int)round(avg);
    string binary = "";
    while(int_avg > 0){
        binary = (char)(int_avg % 2 + '0') + binary;
        int_avg /= 2;
    }
    return binary;
}

int main() {
    printf("%s\n",rounded_avg(1,5));  // 11
    printf("%s\n",rounded_avg(7,5));  // -1
    printf("%s\n",rounded_avg(10,20)); // 1111
    printf("%s\n",rounded_avg(20,33)); // 11010
    return 0;
} 
