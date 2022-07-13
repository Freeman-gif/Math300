%% varaible

l = 10
h =1/N
N =10
f(1) = 0
%%funciton
%n os the dependent variable 
for n = 1:N
   f(n+1) = f(n)+h*(n^2 + 1) 
    
end

x = linspace(0,l,N)
plot(x,f)
    