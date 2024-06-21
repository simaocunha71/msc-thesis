"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""
import heapq

def heap_queue_largest(nums, k):
    h = [] # a list to store the largest elements from nums
    for _ in range(0,k):
        print("poping from the end")
        nxt = heapq.heappop(h)
        print("removed element " + str(nxt))
    for n in range(0, k-1):
        print("pushing into the queue")
        nxt = nums[k] - (nums[k+1:])/2  # we get the largest element and remove it from the end of the list
        heapq.heappush(h,nxt)
        print("placed " + str(nxt))
    return h