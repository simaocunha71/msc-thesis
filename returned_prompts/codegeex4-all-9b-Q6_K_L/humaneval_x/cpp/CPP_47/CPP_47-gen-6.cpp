float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2-1];
t = l[n/2];
return (s+t)/2;
}else{
return l[n/2];
}
B:
float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2-1];
t = l[n/2];
return (s+t)/2;
}else{
return l[n];
}

C:
float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2];
t = l[n/2+1];
return (s+t)/2;
}else{
return l[n/2];
}

D:
float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2-1];
t = l[n/2];
return (s+t)/2;
}else{
return l[n/2+1];
}

E:
float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2-1];
t = l[n/2+1];
return (s+t)/2;
}else{
return l[n/2];
}
F:
float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2-1];
t = l[n/2];
return (s+t)/2;
}else{
return l[n-1];
}
G:
float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2];
t = l[n/2+1];
return (s+t)/2;
}else{
return l[n/2+1];
}

H:
float s = 0.0;
float t = 0.0;
int n = l.size();
if(n%2 == 0){
s = l[n/2];
t = l[n/2+1];
return (s+t)/2;
}else{
return l[n/2