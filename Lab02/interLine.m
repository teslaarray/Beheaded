
Y = [0.031, 0.044, 0.012]; %measured voltage
X = [1.02, 1.5, 0.5]; %calculated I


scatter(X, Y);
hold on
% p = polyfit(X, Y, 1);
% p
% x1 = linspace(X(1), X(length(X)), 1000);
% y1 = polyval(p, x1);
% 
% plot(x1, y1, "red")
% 
xlabel("A");
ylabel("V");