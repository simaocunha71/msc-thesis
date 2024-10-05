    int maxFill(List<List<Integer>> grid, int capacity) {
        int count = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for(List<Integer> row : grid){
            for(int i=0; i<row.size(); i++){
                if(row.get(i) == 1){
                    pq.add(capacity);
                }
            }
        }

        while(!pq.isEmpty()){
            int current = pq.poll();
            if(!pq.isEmpty()){
                if(current == pq.peek()){
                    pq.add(current - 1);
                }
            }
            count++;
        }
        return count;
    }

Here is the solution for this problem. The logic is to add the capacity of bucket to a priority queue for each well in the grid. Then we keep removing the maximum capacity from the priority queue and if the top element in the priority queue is same, we reduce the top element by 1 and add it back to the priority queue. We continue this process until the priority queue is empty. The number of times we are removing elements from the priority queue gives us the minimum number of times we need to lower the buckets.

The time complexity of this solution is O(n log n) because we are using a priority queue and the space complexity is O(n) because we are storing the capacities of the buckets in the priority queue.

I hope this solution helps you. Please let me know if you have any queries.

*/


A: Here is the correct solution:


import java.util.*;
import java.lang.*;

class Solution 
{
    public int maxFill(List<List<Integer>> grid, int capacity) 
    {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int count = 0;
        
        for(List<Integer> row : grid)
        {
            for(int i=0; i<row.size(); i++)
            {
                if(row.get(i