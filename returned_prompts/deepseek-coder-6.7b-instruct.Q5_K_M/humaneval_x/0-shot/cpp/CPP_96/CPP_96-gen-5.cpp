    vector<int> primeList;
    if(n<2) return primeList;
    primeList.push_back(2);

B:
    for(int i=3; i<n; i+=2){
        bool isPrime = true;

C:
        for(int j=0; j<primeList.size(); j++){
            if(i%primeList[j]==0){
                isPrime = false;
                break;
            }
            if(primeList[j]*primeList[j]>i) break;
        }

D:
        if(isPrime) primeList.push_back(i);
    }
    return primeList;
}

int main() {
    vector<int> primeList = count_up_to(18);
    for(int i=0; i<primeList.size(); i++)
        printf("%d ",primeList[i]);
    return 0;
}
```

## 解析

这段代码的功能是生成所有小于给定输入n的素数。

- 在标签A中，我们声明了一个向量来存储素数，并检查n是否小于2。如果是，我们返回一个空向量。
- 在标签B中，我们从3开始循环，每次循环增加2，直到n。这是因为我们知道2是唯一的偶素数。
- 在标签C中，我们检查当前数字i是否能被之前找到的任何素数整除。如果可以，那么它不是素数，我们就跳出循环。如果当前素数的平方大于i，我们也跳出循环。
- 在标签D中，如果我们没有找到任何能整除i的素数，那么i就是一个素数，我们将其添加到我们的素数向量中。
- 最后，我们返回素数向量。

这个算法被称为埃拉托斯特尼筛法，是一种古老的算法，用于找出小于给定限制的所有素数。它通过从第一个素数开始，迭代地标记每个素数的倍数来工作。

注意：由于这个