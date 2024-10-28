    if(number == need){
        vector<int> result;
        result.push_back(number);
        result.push_back(remaining - number);
        return result;
    }
    else if(need > number){
        if(remaining - (need - number) >= 0){
            vector<int> result;
            result.push_back(number + (need - number));
            result.push_back(remaining - (need - number));
            return result;
        }
        else{
            vector<int> result;
            result.push_back(number + remaining);
            result.push_back(0);
            return result;
        }
    }
    else if(need < number){
        if(remaining >= need - number){
            vector<int> result;
            result.push_back(number + (need - number));
            result.push_back(remaining - (need - number));
            return result;
        }
        else{
            vector<int> result;
            result.push_back(number);
            result.push_back(0);
            return result;
        }
    }
}

int main(){
    vector<int> result = eat(5, 6, 10);
    printf("%d %d", result[0], result[1]);
    return 0;
}

*/

























































































































































































