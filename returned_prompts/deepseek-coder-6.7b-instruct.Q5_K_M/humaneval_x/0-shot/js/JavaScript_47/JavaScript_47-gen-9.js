  l.sort((a, b) => a - b)

  let middle = Math.floor(l.length / 2)

  if (l.length % 2 === 0) {
    return (l[middle - 1] + l[middle]) / 2
  } else {
    return l[middle]
  }
}

module.exports = median;
```

### 7.2.2 코드 설명

우선 문제의 조건에 맞게 제일 먼저 해야 할 것은 리스트를 정렬하는 것이다. 이는 sort() 메서드를 사용하여 수행된다. 

정렬된 리스트에서 중간값을 구해야 한다. 그러나 리스트의 길이가 홀수인지 짝수인지에 따라 계산법이 달라진다. 따라서 리스트의 길이를 2로 나눈 몫을 구한다. 이는 리스트 길이가 홀수인 경우