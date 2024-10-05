    vector<float> sorted_l;
    vector<float> even_elements;
    for(int i=0; i<l.size(); i++){
        if(i%2 == 0){
            even_elements.push_back(l[i]);
        }
    }
    sort(even_elements.begin(), even_elements.end());

B:
    for(int i=0, j=0; i<l.size(); i++){
        if(i%2 == 0){
            sorted_l.push_back(even_elements[j]);
            j++;
        } else {
            sorted_l.push_back(l[i]);
        }
    }

C:
    return sorted_l;
}

// Test cases
int main(){
    vector<float> l1 = {1, 2, 3};
    vector<float> l2 = {5, 6, 3, 4};
    vector<float> l1_prime = sort_even(l1);
    vector<float> l2_prime = sort_even(l2);
    for(int i=0; i<l1_prime.size(); i++){
        printf("%.0f, ", l1_prime[i]);
    }
    printf("\n");
    for(int i=0; i<l2_prime.size(); i++){
        printf("%.0f, ", l2_prime[i]);
    }
    printf("\n");
    return 0;
}

*/


















































































































































