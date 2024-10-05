    sort(numbers.begin(), numbers.end());
    for(int i=0; i<numbers.size()-1; i++){
        if(abs(numbers[i] - numbers[i+1]) < threshold)
            return true;
    }
    return false;
}

int main(){
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    printf("%s\n", has_close_elements(numbers1, 0.5) ? "true" : "false");
    vector<float> numbers2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    printf("%s\n", has_close_elements(numbers2, 0.3) ? "true" : "false");
    return 0;
}
*/

*/


// Solution:

