    float mean=0, sum=0;
    for(int i=0;i<numbers.size();i++)
        sum+=numbers[i];
    mean=sum/numbers.size();
    float deviation=0;
    for(int i=0;i<numbers.size();i++)
        deviation+=fabs(numbers[i]-mean);
    return deviation/numbers.size();
}
int main(){
    vector<float> numbers={1.0,2.0,3.0,4.0};
    printf("%f",mean_absolute_deviation(numbers));
    return 0;
}
