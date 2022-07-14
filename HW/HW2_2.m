%% variables

A = [1 1 1; 1 2 3; 1 3 6];
B = [1;-5;2]
C = [1 1 1 1; 1 2 3 -5; 1 3 6 2]%create Augmented matrix




%% functions
det(A)
rank(A)
X = linsolve(A,B)
X_2 = A\B
X_3 = rref(C)%row reduced echelon form