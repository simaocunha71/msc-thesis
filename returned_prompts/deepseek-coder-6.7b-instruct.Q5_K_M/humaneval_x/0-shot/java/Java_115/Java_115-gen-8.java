        int count = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (List<Integer> row : grid) {
            for (int water : row) {
                pq.offer(-water);
            }
        }

B:
        while (!pq.isEmpty()) {
            int water = -pq.poll();
            if (capacity < water) {
                pq.offer(-(water % capacity));
            }
            count += water / capacity;
            if (water % capacity != 0) count++;
        }

C:
        return count;
    }
}
```

A: 우선 우물의 수량을 담을 우선순위 큐를 선언합니다.

B: 큐가 빌 때까지 반복합니다. 큐에서 우물의 수량을 꺼내서 버킷의 용량보다 크면 나머지를 다시 큐에 넣고, 버킷의 용량만큼 우물을 비울 수 있는 횟수를 센다.

C: 그리고 버킷을 비우는 횟수를 반환한다.

문제의 조건