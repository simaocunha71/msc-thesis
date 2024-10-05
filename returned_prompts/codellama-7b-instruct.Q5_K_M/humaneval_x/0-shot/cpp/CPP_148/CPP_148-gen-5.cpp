
}
int main(int argc, char const *argv[])
{
    vector<string> result = bf("Jupiter", "Neptune");
    for(int i=0;i<result.size();i++){
        printf("%s ",result[i].c_str());
    }
    printf("\n");
    return 0;
}
