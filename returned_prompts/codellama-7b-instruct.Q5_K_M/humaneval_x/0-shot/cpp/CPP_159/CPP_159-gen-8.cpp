    vector<int> result;
    result.push_back(number + remaining);
    result.push_back(0);
    return result;
}

int main(){
    vector<int> result = eat(5, 6, 10);
    for(auto i: result){
        printf("%d ",i);
    }
    printf("\n");
}
