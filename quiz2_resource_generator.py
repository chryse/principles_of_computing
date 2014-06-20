"""
Simulator for resource generation with upgrades
"""

import simpleplot
import math
import codeskulptor
codeskulptor.set_timeout(20)


def resources_vs_time(upgrade_cost_increment, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    resources_vs_time = []
    time_at_purchase = 0
    total_cost = 1
    rate = 1
    total_resource_generated = 1
    for upgrade in range(num_upgrade):
        time_at_purchase += total_cost / rate
        resources_vs_time.append([time_at_purchase, total_resource_generated])
        total_cost += upgrade_cost_increment
        total_resource_generated += total_cost
        rate += 1
        
    return resources_vs_time

def resources_vs_time_cookie(upgrade_cost_increment, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    resources_vs_time = []
    time_at_purchase = 0
    total_cost = 1
    rate = 1
    total_resource_generated = 1
    for upgrade in range(num_upgrade):
        time_at_purchase += total_cost / rate
        resources_vs_time.append([time_at_purchase, total_resource_generated])
        total_cost += upgrade_cost_increment * 1.15
        total_resource_generated += total_cost
        rate += 1
        
    return resources_vs_time


def test():
    """
    Testing code for resources_vs_time
    """
    #data1 = resources_vs_time(0.5, 20)
    #data2 = resources_vs_time(1.5, 10)
    
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2])
    
    
    '''
    Question 1
    The following file includes a template for your function 
    as well as several test examples and answers. 
    The first entry in output list should always be [1.0, 1.0] 
    and the length of the list should be exactly num_upgrades. 
    Once your implementation matches the provided test data, 
    compute resources_vs_time (upgrade_cost_increment, 10) 
    for upgrade_cost_increment equal to 0.0 and 1.0. 
    Then enter the total resources generated after ten upgrades 
    as computed by each of these calls in the box below. 
    You should enter the answer as exactly two numbers separated 
    by a space. (Don't use parentheses, brackets, or commas 
    to group the two numbers together.)
    10, 55
    '''
    #q1_ex1 = resources_vs_time(0.0, 10)
    #q1_ex2 = resources_vs_time(1.0, 10)
    #print q1_ex1
    #print q1_ex2
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [q1_ex1, q1_ex2])

    '''
    Question 2
    Use the SimplePlot library for CodeSkulptor 
    to plot the graph of total resources generated 
    as a function of time for upgrade_cost_increment= 0, 0.5, 1, 2. 
    Which value for upgrade_cost_increment generates the fastest growth 
    in total resources?
    0.0
    '''
    #q2_ex1 = resources_vs_time(0.0, 10)
    #q2_ex2 = resources_vs_time(0.5, 10)
    #q2_ex3 = resources_vs_time(1.0, 10)
    #q2_ex4 = resources_vs_time(2.0, 10)
    #print q2_ex1
    #print q2_ex2
    #print q2_ex3
    #print q2_ex4
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [q2_ex1, q2_ex2, q2_ex3, q2_ex4])

    '''
    Question 3 
    The next four questions will examine the case 
    when upgrade_cost_increment== 0. 
    We first consider whether the total resources generated is 
    a polynomial function of time for this case. 
    To answer this question, generate the Log/Log plot of this graph 
    by modifying resources_vs_time to take the logarithm of 
    current_time and total_resources_generated (using math.log()).
    Then use SimplePlot to plot the output and examine the resulting graph. 
    Is the graph a straight line? No
    '''
    #from math import log
    #q3_ex1 = resources_vs_time(0.0, 10)
    #q3_ex1_log = [[log(q3_ex1[i][0]), log(q3_ex1[i][1])] for i in range(len(q3_ex1))]
    #print q3_ex1
    #print q3_ex1_log
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [q3_ex1_log])
    
    '''
    Question 4
    Examine the output of resources_vs_time for the case 
    when upgrade_cost_increment == 0.
    What arithmetic sum models the value of current_time after n upgrades?
    1, 1.5, 1.833333, 2.083333, 2.2833333, 2.45, 2.592857, 2.717857, 2.82896, 2.92896
    1 + 1/2 + 1/3 + ... + 1/n
    '''
    #q4_ex = resources_vs_time(0.0, 10)
    #print q4_ex
    
    '''
    Question 5
    What function f(n) models the total value of the sum 
    in problem 4 most accurately?
    Hint: the most accurate approximation will always be within 
    a small fixed amount of the value of 
    the sum for any value of n.
    f(n) = log(n)
    '''
    
    '''
    Question 6
    To conclude our analysis of this case, 
    we wish to express total resources generated in terms of time. 
    Examining the output when upgrade_cost_increment == 0, 
    we observe that the total resources after n upgrades is simply n. 
    Based on this observation, we observe that we can easily express 
    the time t as a function of the resources r via t=f(r) 
    where f() was the solution to problem 5. 
    To model the total resources as a function of time, 
    we seek a function g() that relates total resources r 
    to the time t via r=g(t).

    Enter g(t) as a math expression. 
    To format your expression correctly, 
    please consult this page. 
    Remember to use the Preview button 
    (as well as the Help link) to make sure that your expression 
    is formatted correctly.
    r = E^t = math.exp(t) = math.pow(math.e, t)
    '''
    
    '''
    Question 7
    For the next three problems, we will consider the case 
    when upgrade_cost_increment == 1.
    Plotting the output of resources_vs_time() in Log/Log form 
    yields a graph which is nearly a straight line. 
    This observation signals that the function may be 
    a polynomial function. Compute the slope of this line 
    and round it to the nearest integer to estimate 
    the degree of the polynomial.
    2
    '''
    #q7 = resources_vs_time(1.0, 5)
    #q7_log = [[math.log(q7[i][0]), math.log(q7[i][1])] for i in range(len(q7))]
    
    #slope = []
    #new_q7 = list(q7_log)
    #for i in range(len(q7)-1):
    #    slope.append(round((q7_log[i][1] - new_q7[i+1][1]) / (q7_log[i][0] - new_q7[i+1][0])))
    
    #print q7
    #print q7_log
    #print slope # answer is 2
    #print (q7_log[0][1] - new_q7[1][1]) / (q7_log[0][0] - new_q7[1][0])
    #print (q7_log[1][1] - new_q7[2][1]) / (q7_log[1][0] - new_q7[2][0])
    #print (q7_log[2][1] - new_q7[3][1]) / (q7_log[2][0] - new_q7[3][0])
    #print (q7_log[3][1] - new_q7[4][1]) / (q7_log[3][0] - new_q7[4][0])

    
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [q7_log])
    
    '''
    Question 8
    Examining the output of resources_vs_time(), 
    what sum models the total resources generated after n upgrades?
    1 + 2 + 3 + ... + n
    '''
    q8 = resources_vs_time(1.0, 10)
    print q8
    
    '''
    Question 9
    For upgrade_cost_increment == 1, 
    examine the relationship between the time t and the number of upgrades n. 
    Then, derive an exact expression for total resources generated 
    in terms of the time t. 
    Enter this expression in t as a math expression below.
    n * (n+1) * 1/2
    t * (t+1) * 1/2
    '''
    
    
    '''
    Question 10
    In the last two questions, we will analyze the total resources generated 
    in Cookie Clicker when there is only one possible upgrade option. 
    Instead of increasing the cost of an upgrade by some fixed amount 
    after each upgrade, each upgrade in Cookie Clicker costs 15% more than 
    the cost of the previous upgrade. 
    (Note that this cost compounds in the same manner that interest does.)
    
    If the first upgrade costs one unit, enter a math expression 
    that models the cost of the nth upgrade.
    1.15 ^ (n-1) = math.pow(1.15, n-1)
    '''
    
    '''
    Question 11
    For the case when upgrade_cost_increment == 1, 
    we earlier observed that total resources generated grew 
    as a quadratic function of time. 
    When we compare this case to the behavior of Cookie Clicker 
    from question 10, which of the following statements is true?
    You may want to compute and plot some examples using SimplePlot 
    to help in making this comparison.
    Answer:
    After some fixed amount of time, 
    the upgrade_cost_increment == 1 case always generates 
    more total resources than the Cookie Clicker case.
    '''
    #q11_cost1 = resources_vs_time(1.0, 10)
    #q11_cost2 = resources_vs_time_cookie(1.0, 10)
    #print q11_cost1
    #print q11_cost2
    
    #simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [q11_cost1, q11_cost2])
    
test()


# Sample output from the print statements for data1 and data2
#[[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
#[[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]
