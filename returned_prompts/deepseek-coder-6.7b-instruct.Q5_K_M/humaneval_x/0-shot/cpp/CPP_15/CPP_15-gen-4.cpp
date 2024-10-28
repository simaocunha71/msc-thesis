    string sequence="";
    for(int i=0;i<=n;i++){
        sequence += to_string(i);
        if(i<n)
            sequence += " ";
    }
    return sequence;
}

int main() {
    printf("%s", string_sequence(5).c_str());
    return 0;
}

