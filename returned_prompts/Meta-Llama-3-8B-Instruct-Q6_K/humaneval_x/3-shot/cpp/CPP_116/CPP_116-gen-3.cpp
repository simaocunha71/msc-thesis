    sort(arr.begin(), arr.end(), [](int a, int b){
        if (bitset<32>(a).count() != bitset<32>(b).count())
            return bitset<32>(a).count() < bitset<32>(b).count();
        return a < b;
    });
    return arr;
}
// The bitset<32>(a) is used to convert the integer to a binary number
// The count function is used to count the number of ones in the binary representation
// The sort function is used to sort the array based on the number of ones in the binary representation and then based on the decimal value.