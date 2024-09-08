    int start1=interval1[0];
    int end1=interval1[1];
    int start2=interval2[0];
    int end2=interval2[1];
    int start=start1;
    int end=end1;
    if(start1>start2){
        start=start2;
    }
    if(end1<end2){
        end=end2;
    }
    int length=end-start+1;
    if(length<2){
        return "NO";
    }
    for(int i=2; i<=sqrt(length); i++){
        if(length%i==0){
            return "NO";
        }
    }
    return "YES";
}

int main(){
    vector<int> interval1={1,3};
    vector<int> interval2={2,4};
    printf("%s\n",intersection(interval1,interval2).c_str());
    return 0;
}
*/

