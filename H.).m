% Define the data points
x = [1 2 3 4 5 6];
y = [5.5 43.1 128 290.7 498.4 978.67];

% Fit a 4th-degree polynomial
p = polyfit(x, y, 4);

% Define evaluation points
x2 = 1:1:6;

% Evaluate the polynomial at the defined points
y2 = polyval(p, x2);

% Plot the original data points and the fitted polynomial
figure; % Create a new figure
plot(x, y, 'o', x2, y2, '-');
grid on;
xlabel('x');
ylabel('y');
title('Polynomial Fit');
legend('Data Points', 'Fitted Polynomial');
