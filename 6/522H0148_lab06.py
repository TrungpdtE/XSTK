import math
import matplotlib.pyplot as plt

def  pmf_bernoulli(p,x):
  if x == 1:
    return p
  elif x == 0:
    return 1-p
  else:
    return 0

p = 0.5
x= 1

pmf = pmf_bernoulli(p,x)
print(pmf)

def plot_pmf_bernoulli(p):
  X = [0, 1]
  P_bernoulli = [pmf_bernoulli(p,x) for x in X]
  plt.plot(X, P_bernoulli,'o')

  plt.title('PMF of Bernoulli(p = %.2f)' %(p))
  plt.xlabel('Value')
  plt.ylabel('Probality')
  plt.show()

plot_pmf_bernoulli(0.5)

#Binomial distribution
#example

import math
import matplotlib.pyplot as plt

def pmf_binom(k,n,p):
  if k < 0  or k > n: return -1;

  biniomal =  math.comb(n,k)
  p_k = biniomal * math.pow(p,k) * math.pow((1-p),(n-k))
  return p_k

n = 15
k = 4
p = 0.5
binom=pmf_binom(k,n,p)
print(binom)

def  plot_pmf_binom(n,p):
  K = list(range(0,n+1))
  P_binom = [pmf_binom(k,n,p) for k in K]
  plt.plot(K,P_binom,'-o')
  axes = plt.gca()
  axes.set_xlim([0,n])
  axes.set_ylim([0,1.1 * max(P_binom)])
  plt.title('PMF of Bin (%i , %.2f)' %(n,p))
  plt.xlabel('Number k of successes')
  plt.ylabel('Probality of k successes')
  plt.show()

plot_pmf_binom(15,0.5)

#Poison distribution
#example

import math
import matplotlib.pyplot as plt

def pmf_poisson(k,lam):
  poisson = (math.pow(lam,k) * math.pow(math.e,-lam))/ math.factorial(k)
  return poisson

lam = 5
k = 10
pmf_poisson(k,lam)

def plot_pmf_poisson(n,lam):
  K = list(range(0, n+1))
  P_poisson = [pmf_poisson(k,lam) for k in K]
  plt.plot(K, P_poisson, '-o')
  plt.title('PMF of Poisson(%i)' %lam)
  plt.xlabel('Number of events')
  plt.ylabel('Probality of Number of Events')
  plt.show()

plot_pmf_poisson(25,5)

#Geometric distribution
#example

import math
import matplotlib.pyplot as plt

def pmf_geo(p,x):
  p_x = p*math.pow((1-p),x-1)
  return p_x

p = 0.3
x = 5
pmf_geo(p,x)

def plot_pmf_geo(p,n):
  X = list(range(0,n+1))
  P_geo = [pmf_geo(p,x) for x in X]
  plt.plot(X, P_geo, '-o')
  plt.title('PMF of Geo(%.1f)' %p)
  plt.xlabel('Number of events')
  plt.ylabel('Probality of Number of Events')
  plt.show()

plot_pmf_geo(0.3,10)

#ex1

import math
import matplotlib.pyplot as plt

def pmf_binom(k,n,p):
  if k < 0  or k > n: return -1;

  biniomal =  math.comb(n,k)
  p_k = biniomal * math.pow(p,k) * math.pow((1-p),(n-k))
  return p_k

n = 5
k = 2
p = 0.1
binom=pmf_binom(k,n,p)
print(binom)

def  plot_pmf_binom(n,p):
  X = list(range(0,n+1))
  P_binom = [pmf_binom(k,n,p) for k in X]
  plt.plot(X,P_binom,'-o')
  axes = plt.gca()
  axes.set_xlim([0,n])
  axes.set_ylim([0,1.1 * max(P_binom)])
  plt.title('PMF of Bin (%i , %.1f)' %(n,p))
  plt.xlabel('Number k of successes')
  plt.ylabel('Probality of k successes')
  plt.show()

plot_pmf_binom(5,0.1)

#ex2

import math
import matplotlib.pyplot as plt

def pmf_poisson(k,lam):
  poisson = (math.pow(lam,k) * math.pow(math.e,-lam))/ math.factorial(k)
  return poisson

lam = 3
k = 2
poisson = pmf_poisson(k,lam)
print(poisson)

def plot_pmf_poisson(n,lam):
  K = list(range(0, n+1))
  P_poisson = [pmf_poisson(k,lam) for k in K]
  plt.plot(K, P_poisson, '-o')
  plt.title('PMF of Poisson(%i)' %lam)
  plt.xlabel('Number of events')
  plt.ylabel('Probality of Number of Events')
  plt.show()

plot_pmf_poisson(5,3)

#ex3

import math
import matplotlib.pyplot as plt

def pmf_geo(p,x):
  p_x = p*math.pow((1-p),x-1)
  return p_x

p = 0.4
x = 3
result = pmf_geo(p,x)
print(result)

def plot_pmf_geo(p,n):
  X = list(range(0,n+1))
  P_geo = [pmf_geo(p,x) for x in X]
  plt.plot(X, P_geo, '-o')
  plt.title('PMF of Geo(%.1f)' %p)
  plt.xlabel('Number of events')
  plt.ylabel('Probality of Number of Events')
  plt.show()

plot_pmf_geo(0.4,10)