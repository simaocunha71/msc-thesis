
The code you have posted is not complete. There is a missing main function to test your code. I would suggest to write the main function as follows:
int main(){
    vector<float> numbers={1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    float threshold = 0.3;
    if(has_close_elements(numbers, threshold)){
        printf("true\n");
    } else {
        printf("false\n");
    }
    return 0;
}

The other questions are incomplete too. Please provide the input and output for each question to write the code correctly.