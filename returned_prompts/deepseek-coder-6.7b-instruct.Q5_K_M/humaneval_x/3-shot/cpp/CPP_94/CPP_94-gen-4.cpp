    int i;
    int max_prime=0;
    for(i=0;i<lst.size();i++)
    {
        if(is_prime(lst[i]) && lst[i]>max_prime)
        max_prime=lst[i];
    }
    return sum_of_digits(max_prime);
}
bool is_prime(int n){
    if  (n<=1) 
    return false;
    if  (n==2) 
    return true;
    if  (n%2==0) 
    return false;
    for  (int i=3; i*i<=n; i+=2)
    if  (n%i==0) 
    return false;
    return true;
}
int sum_of_digits(int n){
    int sum = 0;
    while (n != 0) {
        sum = sum + n % 10;
        n = n / 10;
    }
    return sum;
}


A: All the codes are correct, you are just missing the main function to call these functions. Here is how you can call the functions:

int main() {
    // Call has_close_elements function
    vector<float> numbers1 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    float threshold1 = 0.3;
    if (has_close_elements(numbers1, threshold1)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    // Call separate_paren_groups function
    string paren_string = "(  )  (( ))  (( )( ))";
    vector<string> result = separate_paren_groups(paren_string);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }

    // Call truncate_number function
    float number = 3.5;
    cout << truncate_