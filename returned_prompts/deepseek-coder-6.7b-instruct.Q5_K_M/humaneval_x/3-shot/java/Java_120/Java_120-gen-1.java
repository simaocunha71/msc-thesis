        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        queue.addAll(arr);
        List<Integer> result = new ArrayList<>();

        for(int i=0; i<k; i++){
            result.add(queue.poll());
        }
        return result;
     }
}

