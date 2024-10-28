    def pluck(arr):
        smallest = None
        smallest_index = None
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and (smallest == None or arr[i] < smallest):
                smallest = arr[i]
                smallest_index = i
        if smallest != None:
            return [smallest, smallest_index]
        else:
            return []


