return s0==s1;
B:
return s0.size()==s1.size() && count(s1.begin(),s1.end(),s0[0])==count(s0.begin(),s1.end(),s0[0]);
C:
return s0==s1;
D:
return s0.size()==s1.size() && s0.find(s1[0])!=string::npos && s1.find(s0[0])!=string::npos;
E:
return s0==s1;
F:
return s0.size()==s1.size() && count(s1.begin(),s1.end(),s0[0])==count(s0.begin(),s1.end(),s0[0]) && s0.find(s1[0])!=string::npos && s1.find(s0[0])!=string::npos;
G:
return s0==s1;
H:
return s0.size()==s1.size() && count(s1.begin(),s1.end(),s0[0])==count(s0.begin(),s1.end(),s0[0]) && s0.find(s1[0])!=string::npos && s1.find(s0[0])!=string::npos && s0==s1;
