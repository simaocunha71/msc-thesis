    if(a < b) goto B;     // jump to label B
    else if(b == 0) return a;
    else goto A;          // jump back to label A
B:
    if(b < a) goto C;     // jump to label C
    else if(a == 0) return b;
    else goto B;          // jump back to label B
C:
    if(b < a) goto D;     // jump to label D
    else if(a % b == 0) return b;
    else goto C;          // jump back to label C
D:
    if(a < b) goto E;     // jump to label E
    else if(b % a == 0) return a;
    else goto D;          // jump back to label D
E:
    if(a < b) goto F;     // jump to label F
    else if(b % a == 0) return a;
    else goto E;          // jump back to label E
F:
    if(b < a) goto G;     // jump to label G
    else if(a % b == 0) return b;
    else goto F;          // jump back to label F
G:
    if(a < b) goto H;     // jump to label H
    else if(b % a == 0) return a;
    else goto G;          // jump back to label G
H:
    if(a < b) goto I;     // jump to label I
    else if(b % a == 0) return a;
    else goto H;          // jump back to label H
I:
    if(a < b) goto J;     // jump to label J
    else if(b % a == 0) return a;
    else goto I;          // jump back to label I
J:
    if(a < b) goto K;     // jump to label K
    else if(b % a == 0) return a;
    else goto J;          // jump back to label J
K:
    if(a < b) goto L;     // jump to label L
    else if(b % a == 0) return a;
    else goto K