    float max = l[0];
    for(int i=0; i<l.size();i++){
        if(l[i]>max){
            max = l[i];
        }
    }
    return max;
}
*/

int main() {

    vector<float> l = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    printf("%f\n", max_element(l));
    return 0;
}

//