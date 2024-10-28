    int sum=0, product=1;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    vector<int> sum_product;
    sum_product.push_back(sum);
    sum_product.push_back(product);
    return sum_product;
}

