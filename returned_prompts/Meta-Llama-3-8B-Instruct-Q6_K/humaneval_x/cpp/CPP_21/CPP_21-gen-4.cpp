    // Find the smallest and largest numbers in the vector
    float smallest = *min_element(numbers.begin(), numbers.end());
    float largest = *max_element(numbers.begin(), numbers.end());

    // Apply the linear transform
    vector<float> result;
    for(float num : numbers){
        result.push_back((num - smallest) / (largest - smallest));
    }
    return result;
}
int main()
{
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> result = rescale_to_unit(numbers);
    for(float num : result)
        printf("%f ",num);
    return 0;
}

