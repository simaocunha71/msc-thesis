    int eaten = number + need;
    int left = remaining - need;
    if(left < 0){
        eaten += remaining;
        left = 0;
    }
    vector<int> result;
    result.push_back(eaten);
    result.push_back(left);
    return result;
}
int main(){
    vector<int> res = eat(5,6,10);
    printf("Total number of eaten carrots: %d\n", res[0]);
    printf("Number of carrots left after meals: %d\n", res[1]);
    return 0;
}
B:
    return 0;
}
C:
    printf("Total number of eaten carrots: %d\n", res[0]);
    printf("Number of carrots left after meals: %d\n", res[1]);
    return 0;
}
D:
    return 0; } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } }