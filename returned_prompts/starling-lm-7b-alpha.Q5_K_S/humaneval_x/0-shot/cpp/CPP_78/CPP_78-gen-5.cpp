    if(num.empty()) return 0;
    if(num.size()==1) {
        if(num=="0"||num=="1"||num=="4"||num=="6"||num=="9") return 0;
        else return 1;
    }
    if(num[0]=='0') return hex_key(num.substr(1));
    if(num[0]=='1') {
        if(num[1]=='0') return 0;
        else if(num[1]=='1') return 0;
        else if(num[1]=='4') return 0;
        else if(num[1]=='6') return 0;
        else if(num[1]=='9') return 0;
        else return 1+hex_key(num.substr(1));
    }
    if(num[0]=='2') return 0;
    if(num[0]=='3') return 1+hex_key(num.substr(1));
    if(num[0]=='5') return 1+hex_key(num.substr(1));
    if(num[0]=='7') return 1+hex_key(num.substr(1));
    if(num[0]=='8') return 0;
    if(num[0]=='9') return 0;
    if(num[0]=='A') return 1+hex_key(num.substr(1));
    if(num[0]=='B') return 1+hex_key(num.substr(1));
    if(num[0]=='C') return 1+hex_key(num.substr(1));
    if(num[0]=='D') return 1+hex_key(num.substr(1));
    if(num[0]=='E') return 1+hex_key(num.substr(1));
    if(num[0]=='F') return 0;
}
int main()
{
    string num;
    while(cin>>num) {
        int count=hex_key