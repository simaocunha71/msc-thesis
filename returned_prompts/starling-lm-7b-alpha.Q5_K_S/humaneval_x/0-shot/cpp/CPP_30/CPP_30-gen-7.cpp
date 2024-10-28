    vector<float> result;
    for(int i = 0; i < l.size(); i++){
        if(l[i] % 2 != 0){
            result.push_back(l[i]);
        }
    }
    return result;
}



/*
Return only numbers in the vector that are multiples of 3.
>>> get_multiples_of_three({1, 2, 3, 4, 5, 6, 7, 8, 9})
{3, 6, 9}
>>> get_multiples_of_three({5,