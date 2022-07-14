%% variables

A = [1 1; 1 2 ; 1 3];
B = [1;5;10];

C = [1 1 1; 1 2 5 ; 1 3 10];%create Augmented matrix
C
%% Functions

rank(A)
rank(B)
X_3 = rref(C)%row reduced echelon form
X = C(:,1);
Y = C(:,2);
Z = C(:,3);
figure; plot3(X,Y,Z,'.-');

