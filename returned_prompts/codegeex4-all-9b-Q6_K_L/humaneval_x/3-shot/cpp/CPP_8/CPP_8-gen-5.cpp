    int i,sum=0,prod=1;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        prod*=numbers[i];
    }
    vector<int> sums_product;
    sums_product.push_back(sum);
    sums_product.push_back(prod);
    return sums_product;
}

