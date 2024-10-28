    float sum = 0;
    for(int i=0; i<numbers.size(); i++)
    {
        sum += numbers[i];
    }

    float mean = sum / numbers.size();

    float mad = 0;
    for(int i=0; i<numbers.size(); i++)
    {
        mad += abs(numbers[i] - mean);
    }

    return mad / numbers.size();
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("%f\n", mean_absolute_deviation(numbers));
}

*/

