    string sequence = "";
    for(int i=0; i<=n; i++){
        if(i == n){
            sequence += to_string(i);
        }else{
            sequence += to_string(i) + " ";
        }
    }
    return sequence;
}

int main() {
    printf("%s\n", string_sequence(0).c_str());
    printf("%s\n", string_sequence(5).c_str());
    return 0;
}


