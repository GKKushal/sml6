import numpy as np 
from statsmodels.stats.proportion import proportions_ztest 
# Given data 
successes = np.array([120, 150])  # number of sales for A and B 
n = np.array([1000, 1200])        
alpha = 0.05                       
# number of users for A and B 
# significance level 


# Perform two-proportion z-test 
z_stat, p_value = proportions_ztest(successes, n) 
# Print results 
print(f"Z-statistic: {z_stat:.3f}") 
print(f"P-value: {p_value:.5f}") 
# Conclusion 
if p_value < alpha: 
    print("Reject the null hypothesis: There is a significant difference in conversion rates between A and B.")  

else: 
    print("Fail to reject the null hypothesis: No significant difference in conversion rates between A and B.")
