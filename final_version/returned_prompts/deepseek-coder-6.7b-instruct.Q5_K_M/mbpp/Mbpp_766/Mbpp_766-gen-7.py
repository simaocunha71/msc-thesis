def longest_increasing_subseq(lst):
    if not lst:
        return []

    seqs = [[lst[0]]]
    for num in lst[1:]:
        seqs.append([num])
        for i in range(len(seqs) - 1):
            if seqs[i][-1] < num and len(seqs[i]) > len(seqs[i + 1]):
                seqs[i + 1] = seqs[i] + [num]
            elif seqs[i][-1] < num and len(seqs[i]) == len(seqs[i + 1]):
                seqs[i + 1] = seqs