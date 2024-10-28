    vector<int> max_val;
    int i,j,temp;
    for(i=0;i<k;i++){
        max_val.push_back(arr[i]);
    }
    for(j=0;j<k;j++){
        for(i=j+1;i<k;i++){
            if(max_val[i]>max_val[j]){
                temp = max_val[j];
                max_val[j] = max_val[i];
                max_val[i] = temp;
            }
        }
    }
    return max_val;
}

// 排序，把最大的放到第一个，然后把剩余的放在后面，然后把剩余的排序，最后再把前面的放回去



// 排序
// 把最大的放到第一个
// 然后把剩余的