    return xs;
}
int main()
{
    vector<float> xs;
    for(int i=0;i<5;i++){
        float x;
        scanf("%f",&x);
        xs.push_back(x);
    }
    vector<float> ys = derivative(xs);
    for(int i=0;i<ys.size();i++){
        printf("%f ",ys[i]);
    }
    return 0;
}

