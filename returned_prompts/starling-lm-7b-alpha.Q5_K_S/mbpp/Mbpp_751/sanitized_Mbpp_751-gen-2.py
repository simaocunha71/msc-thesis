def check_min_heap(heap):
    def _check(start, end):
        if start >= end:
            return True