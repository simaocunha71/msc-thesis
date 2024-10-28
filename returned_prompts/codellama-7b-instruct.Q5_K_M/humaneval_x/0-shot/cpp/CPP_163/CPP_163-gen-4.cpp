    return vector<int>{};

}

int main(){
    vector<int> r = generate_integers(2, 8);
    for(int i = 0; i < r.size(); i++){
        printf("%d ", r[i]);
    }
}
