    vector<float> all_deri;

    for (int i=1;i<xs.size();i++)
    {
        all_deri.push_back(xs[i]*i);
    }

    return all_deri;
}

