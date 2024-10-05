    vector<float> derv;
    int i;
    for(i=1; i<xs.size(); i++){
        derv.push_back(xs[i]*i);
    }
    return derv;
}


int main(){
    vector<float> coeffs = {3, 1, 2, 4, 5};
    vector<float> derv = derivative(coeffs);
    for(int i=0; i<derv.size(); i++){
        printf("%.0f ", derv[i]);
    }
    return 0;
}

*/

*/

In this code, the function `derivative