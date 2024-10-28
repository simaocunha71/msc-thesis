    string arr[1000];
    string temp="";
    int j=0;
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            arr[j]=temp;
            j++;
            temp="";
        }
        else{
            temp+=s[i];
        }
    }
    arr[j]=temp;
    j++;

    for(int i=0;i<j;i++){
        sort(arr[i].begin(),arr[i].end());
    }

    string result="";
    for(int i=0;i<j;i++){
        result+=arr[i];
        if(i<j-1){
            result+=" ";
        }
    }

    return result;
}
*/

int main() {
    string s;
    getline(cin,s);
    string out = anti_shuffle(s);
    cout << out;
}


