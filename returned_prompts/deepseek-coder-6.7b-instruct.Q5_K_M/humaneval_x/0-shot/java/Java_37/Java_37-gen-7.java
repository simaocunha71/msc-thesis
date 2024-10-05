        List<Integer> result = new ArrayList<>();
        List<Integer> evenIdxNums = new ArrayList<>();

        for(int i = 0; i < l.size(); i++) {
            if(i % 2 == 0) {
                result.add(l.get(i));
            } else {
                evenIdxNums.add(l.get(i));
            }
        }

        Collections.sort(evenIdxNums);

        for(int i = 0, j = 0; i < l.size(); i++) {
            if(i % 2 == 0) {
                result.set(i, evenIdxNums.get(j++));
            }
        }

        return result;
    }
}

```

## 4. 프로그래머스 - 최솟값 만들기

문제: 길이가 같은 배열 A와 B가 있습니다. 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 뽑은 숫자는 배열에서 제거합니다. 이러한 과정을 거친 후 남은 숫자들을 곱한