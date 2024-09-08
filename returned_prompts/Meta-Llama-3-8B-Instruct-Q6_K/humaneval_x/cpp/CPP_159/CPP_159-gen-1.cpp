    int total = number + need;
    int left = remaining - (need - (total > remaining ? remaining : need));

    return {total, left};
}

int main() {
    printf("%d %d\n",eat(5,6,10)[0],eat(5,6,10)[1]);
    printf("%d %d\n",eat(4,8,9)[0],eat(4,8,9)[1]);
    printf("%d %d\n",eat(1,10,10)[0],eat(1,10,10)[1]);
    printf("%d %d\n",eat(2,11,5)[0],eat(2,11,5)[1]);
    return 0;
}
