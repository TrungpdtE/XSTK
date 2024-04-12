import matplotlib.pyplot as plt
import math

def pmf_binom(k, n, p):
    binomial_coefficient = math.comb(n, k)
    probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    return probability

#1a
n = 5  
p = 0.1  
k = 2
probability_2_broken = pmf_binom(k, n, p)
print(f"(1a) The probability that exactly 2 machines are broken is: {probability_2_broken:.3f}")
#1b
def plot_pmf_binom(n, p):
    K = list(range(0, n + 1))
    P_binom = [pmf_binom(k, n, p) for k in K]
    plt.plot(K, P_binom, '-o')
    axes = plt.gca()
    axes.set_xlim([0, n])
    axes.set_ylim([0, 1.1 * max(P_binom)])
    plt.title('PMF of Bin(%i, %.2f)' % (n, p))
    plt.xlabel('Number of broken machines')
    plt.ylabel('Probability')
    plt.show()
n = 5  
p = 0.1  
plot_pmf_binom(n, p)


#2a
def pmf_poisson(k, lam):
    probability = (math.exp(-lam) * lam ** k) / math.factorial(k)
    return probability
lam = 3
k = 2
probability_2_calls = pmf_poisson(k, lam)
print(f"(2a) The probability of receiving 2 calls in 1 minute is: {probability_2_calls:.3f}")
#2b
def plot_pmf_poisson(lam):
    K = list(range(0, 6))  
    P_poisson = [pmf_poisson(k, lam) for k in K]
    plt.plot(K, P_poisson, '-o')
    plt.title('PMF of Poisson(%.2f)' % lam)
    plt.xlabel('Number of calls')
    plt.ylabel('Probability')
    plt.show()
lam = 3
plot_pmf_poisson(lam)


#3a
p = 0.4
k = 3
probability_hit_in_third_try = (1 - p) ** (k - 1) * p
print(f"(3a) The probability of hitting the target in the third try is: {probability_hit_in_third_try:.3f}")
#3b
def pmf_geo(p, x):
    probability = p * ((1 - p) ** (x - 1))
    return probability
def plot_pmf_geo(p, n):
    x_values = list(range(1, n + 1))
    probability_values = [pmf_geo(p, x) for x in x_values]
    plt.plot(x_values, probability_values, '-o')
    plt.title('PMF of Geometric(%.2f)' % p)
    plt.xlabel('Number of tries')
    plt.ylabel('Probability')
    plt.show()
p = 0.4
n = 10
plot_pmf_geo(p, n)
