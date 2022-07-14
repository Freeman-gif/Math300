%% varaible
N = 100
t = linspace(0,2*pi,N);

x = 1 + cos(2*t);
y = -1 + 3*sin(4*t);

%%function

plot(x,t);
hold on
plot(y,t);