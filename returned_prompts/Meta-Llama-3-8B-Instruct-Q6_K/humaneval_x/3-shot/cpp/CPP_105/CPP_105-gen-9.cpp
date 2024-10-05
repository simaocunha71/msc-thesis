    vector<string> result;
    map<int,string> map1;
    map1[1]="One";
    map1[2]="Two";
    map1[3]="Three";
    map1[4]="Four";
    map1[5]="Five";
    map1[6]="Six";
    map1[7]="Seven";
    map1[8]="Eight";
    map1[9]="Nine";
    
    vector<int> temp;
    for(int i=0;i<arr.size();i++){
        if(arr[i]>=1 && arr[i]<=9){
            temp.push_back(arr[i]);
        }
    }
    sort(temp.begin(),temp.end());
    reverse(temp.begin(),temp.end());
    for(int i=0;i<temp.size();i++){
        result.push_back(map1[temp[i]]);
    }
    return result;
} 
