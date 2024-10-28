        int total = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (List<Integer> row : grid) {
            for (int i : row) {
                if (i == 1) {
                    pq.offer(1);
                }
            }
        }
        while (!pq.isEmpty()) {
            int max = pq.poll();
            if (capacity >= max) {
                capacity -= max;
            } else {
                total += (max - capacity) / capacity;
                capacity = 0;
            }
        }
        return total;
    }
}
```

## 解法思路：

该问题可以通过优先队列（Priority Queue）来解决，优先队列是一种特殊的队列，其元素具有优先级。在这种情况下，优先队列将用于存储每个单元格中的水量。

首先，我们遍历网格的每个单元格，如果单元格包含水，我们将1添加到优先队列中。

然后，我们开始从优先队列中移除最大水量（使用poll()方法）并尝试将其减去桶的容量。如果桶的容量大于或等于最大水量，我们将桶的容量减去最大水量并继续下一个最大水量。如果桶的容量小于最大水量，我们需要将桶填满，这将需要(max - capacity) / capacity次操作。我们将这个值加到操作总数中，并将桶的容量设置为0。

重复这个过程，直到优先队列为空。最后，我们返回操作总数，即我们需要降低桶的次数。

这个解法的时间复杂度是O(nlogn)，其中n是网格中的单元格数。这是因为我们需要遍历所有单元格并将每个单元格的值插入优先队列，这需要O(n)的时间。然后，我们需要从优先队列中移除所有元素，这需要O(nlogn)的时间，因为这是优先队列的操作时间。

这个解法的空间复杂度是O(n