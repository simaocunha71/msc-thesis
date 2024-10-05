    vector<float> positive_numbers;
    for (int i=0;i<l.size();i++)
    {
        if (l[i]>0)
            positive_numbers.push_back(l[i]);
    }
    return positive_numbers;
}  // This function can be simplified to a one-liner: return vector<float>(std::remove_if(l.begin(), l.end(), [](float x){return x <= 0;}), l.end());  // Thanks to @WalterMitty for the suggestion.