vector<float> rescaled;
float min_val = *min_element(numbers.begin(), numbers.end());
float max_val = *max_element(numbers.begin(), numbers.end());
for(float num : numbers) {
    float scaled = (num - min_val) / (max_val - min_val);
    rescaled.push_back(scaled);
}
return rescaled;
}

int main() {
vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
vector<float> rescaled = rescale_to_unit(numbers);
for(float num : rescaled) {
    printf("%f\n", num);
}
return 0;
}

