def maximize_elements(t1, t2):
    assert len(t1) == len(t2), "Both tuples should have the same length"

    result = []
    for i in range(len(t1)):
        assert len(t1[i]) == len(t2[i]), "Both elements in tuples should have the same length"

        result_i = []
        for j in range(len(t1[i])):
            result_i.append(max(t1[i][j], t2[i][j]))

        result.append(tuple(result_i))

    return tuple(result)