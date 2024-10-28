    float mean = 0.0;
    vector<float> differences;
    for(int i=0; i<numbers.size(); i++){
        mean += numbers[i];
    }
    mean = mean / numbers.size();
    for(int i=0; i<numbers.size(); i++){
        differences.push_back(abs(numbers[i]-mean));
    }
    float mad = 0.0;
    for(int i=0; i<differences.size(); i++){
        mad += differences[i];
    }
    mad = mad / differences.size();
    return mad;
}

