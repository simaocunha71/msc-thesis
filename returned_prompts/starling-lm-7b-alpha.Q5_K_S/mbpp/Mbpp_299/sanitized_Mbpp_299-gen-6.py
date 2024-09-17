def max_aggregate(l):
    scores={}
    for i in l:
        if i[0] not in scores:
            scores[i[0]]=i[1]
        else:
            scores[i[0]]+=i[1]
    max_score=max(scores.values())
    for k in scores:
        if scores[k]==max_score:
            return (k,max_score)