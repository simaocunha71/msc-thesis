    vector<float> l_prime = l;
    vector<float> even_indices;
    for(int i=0; i<l.size(); i+=2){
        even_indices.push_back(l[i]);
    }
    sort(even_indices.begin(), even_indices.end());
    for(int i=0, j=0; i<l.size(); i+=2, ++j){
        l_prime[i] = even_indices[j];
    }
    return l_prime;
}

int main(){
    vector<float> l = {5, 6, 3, 4};
    vector<float> l_prime = sort_even(l);
    for(int i=0; i<l_prime.size(); i++){
        printf("%f ", l_prime[i]);
    }
    return 0;
}

This program will take a vector as input, sort the elements at even indices, then place them back into the vector. The original vector will be unchanged, and the sorted vector will be printed.
*/

// C++
/*
