
def sort_array(array):
    def sort(array):
        return sorted(array, reverse=sum(array)%2)
    return sort(array)
