    if(interval1.size()!=2 || interval2.size()!=2){
        return "NO";
    }
    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];
    if(start1 > end2 || start2 > end1){
        return "NO";
    }
    int start = (start1>start2)?start2:start1;
    int end = (end1>end2)?end1:end2;
    int len = end-start;
    if(len<=1){
        return "NO";
    }
    bool is_prime = true;
    for(int i=2;i<len;i++){
        if(len%i==0){
            is_prime = false;
            break;
        }
    }
    if(is_prime){
        return "YES";
    }
    else{
        return "NO";
    }
}
int main(){
    vector<int> interval1 = {1, 2};
    vector<int> interval2 = {2, 3};
    string result = intersection(interval1,interval2);
    printf("%s",result.c_str());
}
