    int sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        sum += ceil(lst[i]) * ceil(lst[i]);
    }
    return sum;
}  //  or return std::inner_product(lst.begin(), lst.end(), lst.begin(), 0, [](float x, float y){return ceil(x)*ceil(x) + ceil(y)*ceil(y);});
//  or return std::accumulate(lst.begin(), lst.end(), 0, [](float x, int sum){return sum + ceil(x)*ceil(x);});
//  or return std::for_each(lst.begin(), lst.end(), [&sum](float x){sum += ceil(x)*ceil(x);});
//  or return std::transform(lst.begin(), lst.end(), lst.begin(), [](float x){return ceil(x)*ceil(x);}).reduce(0);
//  or return std::accumulate(lst.begin(), lst.end(), 0, [](float x, int sum){return sum + ceil(x)*ceil(x);});
//  or return std::for_each(lst.begin(), lst.end(), [&sum](float x){sum += ceil(x)*ceil(x);});
//  or return std::transform(lst.begin(), lst.end(), lst.begin(), [](float x){return ceil(x)*ceil(x);}).reduce(0);
//  or return std::accumulate(lst.begin(), lst.end(), 0, [](float x, int sum){return sum + ceil(x)*ceil(x);});
//  or return std::for_each(lst.begin(), lst.end(), [&sum](float x){sum += ceil(x)*ceil(x);});
//  or return std::transform(lst.begin(), lst.end(), lst.begin(), [](float x){return ceil(x)*ceil(x);}).reduce(0);
//  or return std::accumulate(lst.begin(), lst.end(), 0, [](float x, int sum){return sum + ceil(x)*ceil(x);});
//  or return std::for_each(lst.begin(), lst.end(), [&sum](float x){sum += ceil(x)*ceil(x);});
//  or return std::transform(lst.begin(), lst.end(), lst.begin(), [](float x){return ceil(x)*ceil(x);}).reduce(0);
//  or return std::accumulate(lst.begin(), lst.end(), 0, [](float x, int sum){return sum + ceil(x)*ceil(x);});
//  or return std::for_each(lst.begin(), lst.end(), [&sum