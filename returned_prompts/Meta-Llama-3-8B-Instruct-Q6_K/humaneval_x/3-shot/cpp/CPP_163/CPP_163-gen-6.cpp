    vector<int> even_numbers;
    for(int i = a; i <= b; i++) {
        if(i % 2 == 0) {
            even_numbers.push_back(i);
        }
    }
    return even_numbers;
}  // End of generate_integers function.