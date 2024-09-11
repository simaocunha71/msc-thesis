"""
def heap_sort(numbers):
    def max_heapify(numbers, root_index, heap_size):
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2
        largest = root_index
        if len(numbers) > left_child < heap_size:
            if numbers[largest] < numbers[left_child]:
                largest = left_child
        if len(numbers) > right_child < heap_size:
            if numbers[largest] < numbers[right_child]:
                largest = right_child
        if largest != root_index:
            numbers[root_index], numbers[largest] = numbers[largest], numbers[root_index]
            max_heapify(numbers, largest, heap_size)

    def build_max_heap(numbers):
        last_parent_index = len(numbers) // 2
        for index in reversed(range(last_parent_index)):
            max_heapify(numbers, index, len(numbers))

    def heap_sort(numbers):
        build_max_heap(numbers)
        heap_size = len(numbers)
        for index in reversed(range(1, heap_size)):
            numbers[index], numbers[0] = numbers[0], numbers[index]
            max_heapify(numbers, 0, index)
        return numbers


print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

"""
