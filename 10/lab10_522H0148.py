#ex1
import numpy as np

# Flip two dice 10,000 times
dice_rolls = np.random.randint(1, 7, size=(10000, 2))

# Calculate the sum of the two dice rolls
x = dice_rolls[:, 0] + dice_rolls[:, 1]

# Find the unique values of X
X = np.unique(x)

# Calculate the probability distribution function of X
P = np.zeros(len(X))
for i in range(len(X)):
    P[i] = np.sum(x == X[i]) / 10000

# Calculate the expectation of X
E = np.mean(x)

# Calculate the variance of X
V = np.var(x)

# Calculate the standard deviation of X
SD = np.sqrt(V)

# Print the results
print("Values of random variable X:", X)
print("Probability distribution function of X:", P)
print("Expectation of X:", E)
print("Variance of X:", V)
print("Standard deviation of X:", SD)

#ex2
import math
import numpy as np
import matplotlib.pyplot as plt

def pmf_normal(x, mu, sigma):
    p_x = (1 / (math.sqrt(2 * math.pi * sigma**2))) * math.exp(-(x - mu)**2 / (2 * sigma**2))
    return p_x

def plot_pmf_normal(mu, sigma):
    X = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    P_normal = [pmf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, '-')
    plt.title('PMF of Normal(%.2f, %.2f)' % (mu, sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()

plot_pmf_normal(0, 1.5)

def cdf_normal(x, mu, sigma):
    c_x = 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))
    return c_x

def plot_cdf_normal(mu, sigma):
    X = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    P_normal = [cdf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, '-')
    plt.title('CDF of Normal(%.2f, %.2f)' % (mu, sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()

plot_cdf_normal(0, 1.5)

mu = 3
sigma = 4
lower_bound = 2
upper_bound = 7
probability = cdf_normal(upper_bound, mu, sigma) - cdf_normal(lower_bound, mu, sigma)
print(f'P(2 < X < 7) = {probability}')

#ex3
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("company-sales_data.csv", delimiter=',')

plt.bar(data['month_number'], data['facecream'], label='FaceCream')
plt.bar(data['month_number'], data['facewash'], label='FaceWash', alpha=0.5)  # Using alpha for transparency
plt.title('FaceCream and FaceWash Sales per Month')
plt.xlabel('Month')
plt.ylabel('Units')
plt.legend()
plt.show()

#ex4
import re
import pandas as pd
import matplotlib.pyplot as plt

def word_frequency(text):
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Convert text to lowercase
    text = text.lower()

    # Split text into words
    words = text.split()

    # Create a dictionary to store word frequencies
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Create a Pandas DataFrame from the dictionary
    df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Count'])

    # Sort the DataFrame by count in descending order
    df = df.sort_values(by='Count', ascending=False)

    # Draw a histogram of the word frequencies
    df.plot.hist(bins=30)
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Histogram of Word Frequency')
    plt.show()

# Example usage
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

word_frequency(text)