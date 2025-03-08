def calculate_probability_a_given_b(prior_a, prior_b, conditional_b_given_a):
    return (conditional_b_given_a * prior_a) / prior_b


prior_a = 0.3
prior_b = 0.6
conditional_b_given_a = 0.8
result = calculate_probability_a_given_b(prior_a, prior_b, conditional_b_given_a)
print(result) 