    float temp = 0;
    int temp2 = 0;
    temp = number;
    temp2 = temp;
    temp = temp - temp2;
    return temp;
}

int main(){
    float number = 3.5;
    printf("%f\n",truncate_number(number));
    return 0;
}