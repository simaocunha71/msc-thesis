        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(k, Collections.reverseOrder());
        heap.addAll(arr.subList(0, k));
        for(int i = k; i < arr.size(); i++) {
            if(arr.get(i) > heap.peek()) {
                heap.poll();
                heap.add(arr.get(i));
            }
        }
        return new ArrayList<>(heap);
    }
}

```

## 코드 설명

제시된 문제는 정렬된 숫자 배열에서 가장 큰 k개 숫자를 반환하는 문제입니다. 우선순위 큐를 사용하여 가장 큰 k개 숫자를 추출하고 배열의 나머지 숫자를 비교하여 큐에 다시 추가합니다.

우선순위 큐를 사용하여 가장 큰 숫자를 반환할 수 있습니다. 우선순위 큐는 우선순위가 가장