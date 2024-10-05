    vector<int> lp;
    vector<int> lq;
    vector<int> lr;
    for (int i=0;i<l.size();i++)
    if (i%3==0)
    lp.push_back(l[i]);
    else if (i%3==1)
    lq.push_back(l[i]);
    else
    lr.push_back(l[i]);
    vector<int> lpq;
    vector<int> lqr;
    for (int i=0;i<lp.size();i++)
    lpq.push_back(lp[i]);
    for (int i=0;i<lq.size();i++)
    lpq.push_back(lq[i]);
    for (int i=0;i<lr.size();i++)
    lqr.push_back(lr[i]);
    vector<int> lpqr;
    for (int i=0;i<lpq.size();i++)
    lpqr.push_back(lpq[i]);
    for (int i=0;i<lqr.size();i++)
    lpqr.push_back(lqr[i]);
    return lpqr;
}



