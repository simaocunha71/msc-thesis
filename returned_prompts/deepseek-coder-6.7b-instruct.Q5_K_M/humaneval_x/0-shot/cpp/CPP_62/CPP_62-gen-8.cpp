    for(int i = 1; i < xs.size(); i++){
        xs[i] *= i;
    }
    xs.erase(xs.begin());
    return xs;
}

int main(){
    vector<float> coeff = {3, 1, 2, 4, 5};
    coeff = derivative(coeff);
    for(int i = 0; i < coeff.size(); i++)
        printf("%.0f ", coeff[i]);
    return 0;
}
*/

