    vector<float> pos_nums;
    for (float f : l)
    if (f>0)
    pos_nums.push_back(f);
    return pos_nums;
} // or simply return std::vector<float>(std::remove_if(l.begin(), l.end(), [](float f) { return f <= 0; }), l.end()); 