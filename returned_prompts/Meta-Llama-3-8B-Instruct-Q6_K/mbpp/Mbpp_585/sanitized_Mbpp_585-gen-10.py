from operator import itemgetter
def expensive_items(dataset: list, n: int) -> list:
    dataset.sort(key=itemgetter('price'), reverse=True)
    return dataset[:n]