    for(int i=0;i<arr.size();i++){
        for(int j=i+1;j<arr.size();j++){
            int temp = 0;
            int temp1 = 0;
            int x = arr[i];
            int y = arr[j];
            while(x!=0){
                temp+=x%2;
                x/=2;
            }
            while(y!=0){
                temp1+=y%2;
                y/=2;
            }
            if(temp1<temp){
                arr[i]=arr[j];
                arr[j]=temp;
            }else if(temp1==temp){
                if(arr[i]>arr[j]){
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
        }
    }
    return arr;
B:
    for(int i=0;i<arr.size();i++){
        int temp = 0;
        int x = arr[i];
        while(x!=0){
            temp+=x%2;
            x/=2;
        }
        arr[i]=temp;
    }
    sort(arr.begin(),arr.end());
    return arr;
}
int main(){
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> ans = sort_array(arr);
    for(int i=0;i<ans.size();i++){
        printf("%d ",ans[i]);
    }
    return 0;
}
请问这个代码有什么错误

这段代码的目的是对整数数组进行排序，根据每个整数在二进制表示中1的数量进行排序。然而，代码中有几个错误：

1. 在 `sort_array` 函数的 `A` 部分，尝试使用冒泡排序算法对数组进行排序，但是这个部分有逻辑错误。特别是，在比较 `temp1` 和 `temp` 的时候，应该使用 `temp1` 和 `temp` 来比较，而不是 `arr[i]` 和 `arr[j]`。此外，在交换 `arr[i]` 和 `arr[j]` 的值的时候，应该交换的是 `arr[i]` 和 `arr[j]`，而不是 `arr[i]` 和 `temp`。

2. 在 `sort_array` 函数的 `B` 部分，尝试将数组中的每个整数转换为二进制，并计算其中1的数量。然后，对这个新的数组进行排序。但是，这个部分没有正确地处理负数。在二进制表示中，负数通常使用补码表示