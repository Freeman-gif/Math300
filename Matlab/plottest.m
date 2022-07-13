%%variable
tiledlayout(2,2);
ax1 = nexttile;
sphere(ax1);
axis equal
title('20-by-20 faces (Default)')

ax2 = nexttile;
sphere(ax2,50)
axis equal
title('50-by-50 faces')

ax3 = nexttile;
sphere(ax3,100)
axis equal
title('100-by-100 faces')
%x = -pi:0.1:pi;
%x = linspace(0.3*pi,200)
%y = cos(x) + rand(1,200)
%scatter(x,y);
%%plot
%plot(x,sin(x),'b');
%hold on
%plot(x,cos(x),'r');
%hold on 
%plot([1 2 3 4 5 6],[0 3 1 6 4 10],'--or')

