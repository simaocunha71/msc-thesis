    if(need > remaining){
        number += remaining;
        remaining = 0;
    }else{
        number += need;
        remaining -= need;
    }
    return {number, remaining};
}
int main(){
    int number, need, remaining;
    scanf("%d %d %d", &number, &need, &remaining);
    vector<int> res = eat(number, need, remaining);
    printf("{ %d, %d }\n", res[0], res[1]);
    return 0;
}
```

### 解析
给定一个整数`number`，表示已经吃了多少个胡萝卜，一个整数`need`，表示需要吃多少个胡萝卜，以及一个整数`remaining`，表示剩余的胡萝卜数，你的任务是返回一个包含两个整数的向量`{total, left}`。

其中，`total`是吃过的胡萝卜总数，`left`是剩余的胡萝卜数。如果剩余的胡萝卜数小于需要的胡萝卜数，那么你需要吃完所有剩余的胡萝卜，并且仍然感到饥饿。

这个问题可以通过简单的if-else条件来解决。如果需要的胡萝卜数大于剩余的胡萝卜数，你需要吃掉所有的剩余胡萝卜，并且`total`为`number`加上剩余的胡萝卜数，`left`为0。否则，你吃掉`need`个胡萝卜，`total`为`number`加上`need`，`left`为剩余的胡萝卜数减去`need`。

这个问题主要考察对基本的算术运算和条件语句的理解和应用。

### 测试

```
输入：5 6 10
输出：{11, 4}

输入：4 8 9
输出：{12, 1}

输入：1 10 10
输出：{11, 0}

输入：2 11 5
输出：{7, 0}
```

### 总结

这个问题主要考察对基本的算术运算和条件语句的