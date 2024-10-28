    if(interval1[0]>interval2[1] || interval2[0]>interval1[1])
        return "NO";
    else if(interval1[0]==interval2[0] && interval1[1]==interval2[1])
        return "NO";
    else
        return "YES";

}

int main() {
    vector<int> a={1,2};
    vector<int> b={2,3};
    cout<<intersection(a,b);
    return 0;
}



