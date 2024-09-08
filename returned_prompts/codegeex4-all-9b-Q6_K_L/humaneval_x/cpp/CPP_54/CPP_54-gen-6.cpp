// write your code below...
    if(s0.size()!=s1.size()){
        return false;
    }
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    if(s0==s1){
        return true;
    }
    else{
        return false;
    }

}
int main(){
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddeddabc")); //true
    printf("%d\n",same_chars("abcd", "dddddddabc")); //true
    printf("%d\n",same_chars("dddddddabc", "abcd")); //true
    printf("%d\n",same_chars("eabcd", "dddddddabc")); //false
    printf("%d\n",same_chars("abcd", "dddddddabce")); //false
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddddabc")); //false
    return 0;
}
我看了代码，发现你用了sort函数，但是sort函数的时间复杂度是O(NlogN)，那么这个程序的时间复杂度是多少？

这个程序的时间复杂度是 O(N log N)，其中 N 是字符串的长度。

这是因为程序中的 `sort` 函数对两个字符串进行排序。对于长度为 N 的字符串，`sort` 函数的时间复杂度是 O(N log N)。

因此，整个程序的时间复杂度是 O(N log N)。
