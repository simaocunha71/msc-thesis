vector<int> intersection( vector<int> interval1,vector<int> interval2){
    vector<int> intersection;
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if(start<=end){
        intersection.push_back(start);
        intersection.push_back(end);
    }
    return intersection;
}
string intersection( vector<int> interval1,vector<int> interval2){
    vector<int> intersection = intersection(interval1, interval2);
    if(intersection.size()==0){
        return "NO";
    }else{
        int length = intersection[1]-intersection[0]+1;
        if(length==1){
            return "NO";
        }else if(is_prime(length)){
            return "YES";
        }else{
            return "NO";
        }
    }
}
bool is_prime(int number){
    if(number<=1){
        return false;
    }
    for(int i=2;i<=sqrt(number);i++){
        if(number%i==0){
            return false;
        }
    }
    return true;
}
*/
B:
string intersection( vector<int> interval1,vector<int> interval2){
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if(start<=end){
        int length = end-start+1;
        if(length==1){
            return "NO";
        }else if(is_prime(length)){
            return "YES";
        }else{
            return "NO";
        }
    }else{
        return "NO";
    }
}
bool is_prime(int number){
    if(number<=1){
        return false;
    }
    for(int i=2;i<=sqrt(number);i++){
        if(number%i==0){
            return false;
        }
    }
    return true;
}

C:
string intersection( vector<int> interval1,vector<int> interval2){
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if(start<=end){
        int length = end-start+1;
        if(length==1){
            return "NO";
        }else if(is_prime(length)){
            return "YES";
        }else{
            return "NO";
        }
    }else{
        return "NO";
    }
}
bool is_prime(int number){
    if(number<=1){
        return false;
