    float max = l[0];
    for(int i=0; i < l.size(); i++){
        if(l[i] > max){
            max = l[i];
        }
    }
    return max;
}

int main(){
    vector<float> l = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    printf("%f", max_element(l));
    return 0;
}


A: Your code is mostly correct. There's just one thing you need to consider. The function max_element(vector) should be returning a float value, but in your main function, you're trying to print the result with printf() which expects a string (char*). You should modify the printf line to:
printf("%f", max_element(l));

Also, it's better to use std::max_element algorithm, which is more efficient and less error-prone.
Here's the corrected code:
