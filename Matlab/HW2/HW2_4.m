%% Variables
s = 0; % random number
k = 0; % sum result
n = 20;%set threashold 

%% functions

while k <= n % set condition for while loop, run the loop while sum result is less or equal to 20 
    s = randi(10); % random interger between 1 and 10
    k = s + k; % stack the random interger that we created
    disp(s)
    
end


