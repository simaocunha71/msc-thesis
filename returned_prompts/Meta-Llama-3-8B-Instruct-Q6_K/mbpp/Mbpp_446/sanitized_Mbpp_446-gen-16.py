def count_Occurrence(tuple, elements):
    occurrence_count = {}
    for element in elements:
        occurrence_count[element] = tuple.count(element)
    return occurrence_count