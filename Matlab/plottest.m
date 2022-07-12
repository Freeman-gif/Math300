%%variable
x = -pi:0.1:pi;

%%plot
plot(x,sin(x),'b');
hold on
plot(x,cos(x),'r');
hold on 
plot([1 2 3 4 5 6],[0 3 1 6 4 10],'--or')