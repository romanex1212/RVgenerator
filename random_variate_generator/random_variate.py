from random import random
from numpy import log
from math import ceil, exp, cos, pi
import seaborn as sns
import matplotlib.pyplot as plt

class random_variate:
    '''
    random_variate initiates a random variate generation operation
    '''

    def __init__(self) -> None:
        self.n = 0
        self.distribution = []

    def set_n(self, n: int) -> None:
        '''
        set_n checks if the value provided for n number of variates to generate is
        an integer greater than or equal to zero

        :int n: number of variates to generate
        '''
        if not isinstance(n, int) or n <= 0: 
            raise ValueError("number of variates to generate must be an integer greater than or equal to 1")
        else: 
            self.n = n
    
    def get_n(self):
        '''
        get_n returns n, the number of variates to generate initialized by the class
        '''
        return self.n

    def check_if_greater_than_zero(self, p: float):
        '''
        checks if parameter is greater than zero

        :float p: value to check
        '''
        if p > 0:
            return p
        else:
            raise ValueError("parameter must be greater than zero")

    def check_probability_parameter(self, p: float):
        '''
        checks if probability parameter is greater than or equal to zero and less than or equal to one

        :float p: value to check
        '''
        if p >= 0 and p <= 1:
            return p
        else:
            raise ValueError("parameter must be greater than or equal to zero and less than or equal to one")
        
    def plot(self, plot_title = None) -> None:
        '''
        plot_dist generates a histogram of the distribution

        :str plot_title: plot title
        :bool kde: option to include smoothing line in plot
        '''
        plt.clf()
        sns.histplot(x = self.distribution, stat = 'probability').set(xlabel ="x", 
                                                                      ylabel = "Probability(x)", 
                                                                      title = plot_title)
        plt.show()

    def binomial_variate(self, p: float, n: int):
        '''
        binomial_variate returns random binomial distribution variates
        given that the probability parameter is greater than or equal to zero and less than or equal to one
        if n = 1, the variate is a bernoulli trial
        
        :float p: probability parameter p
        :int n: number of variates to generate
        '''
        self.set_n(n)
        p = self.check_probability_parameter(p)

        if self.n == 1:
            u = random()
            if u <= p:
                return 1
            else:
                return 0
        else:
            dist = []
            for x in range(0,self.n):
                u = random()
                if u <= p:
                    dist.append(1)
                else:
                    dist.append(0)
            self.distribution = dist
            return dist

    def geom_variate(self, p: float, n: int):
        '''
        geom_variate returns random geometric distribution variates
        given that the probability parameter is greater than zero and less than one
        
        :float p: probability parameter p
        :int n: number of variates to generate
        '''
        self.set_n(n)

        if p > 0 and p < 1:
            pass
        else:
            raise ValueError("parameter must be greater than zero and less than one")
        
        if self.n == 1:
            return ceil(log(random())/log(1 - p))
        else:
            dist = []
            for x in range(0,self.n):
                dist.append(ceil(log(random())/log(1 - p)))
            self.distribution = dist
            return dist

    def poisson_variate(self, l: float, n: int):
        '''
        poisson_variate returns random poisson distribution variates
        given that the rate parameter is greater than zero
        
        :float l: rate parameter l
        :int n: number of variates to generate
        '''
        self.set_n(n)
        l = self.check_if_greater_than_zero(l)

        if self.n == 1:
            x = 0
            product_operator_u_i = random()
            while exp(-l) <= product_operator_u_i:
                x += 1
                product_operator_u_i = product_operator_u_i * random()
            return x
        else:
            dist = []
            for x in range(0,self.n):
                x = 0
                product_operator_u_i = random()
                while exp(-l) <= product_operator_u_i:
                    x += 1
                    product_operator_u_i = product_operator_u_i * random()
                dist.append(x)
            self.distribution = dist
            return dist

    def uniform_variate(self, a: float, b: float, n: int):
        '''
        uniform_variate returns random uniform distribution variates
        if a = 0 and b = 1, uniform_variate returns standard uniform distribution variates
        
        :float a: low bound value
        :float b: high bound value
        :int n: number of variates to generate
        '''
        self.set_n(n)

        if self.n == 1:
            return random()*(b - a) + a
        else:
            dist = []
            for x in range(0,self.n):
                dist.append(random()*(b - a) + a)
            self.distribution = dist
            return dist

    def exp_variate(self, l: float, n: int):
        '''
        exp_variate returns random exponential distribution variates
        given that the rate parameter is greater than zero
        
        :float l: rate parameter lambda
        :int n: number of variates to generate
        '''
        self.set_n(n)
        l = self.check_if_greater_than_zero(l)

        if self.n == 1:
            return -(1/l)*log(random())
        else:
            dist = []
            for x in range(0,self.n):
                dist.append(-(1/l)*log(random()))
            self.distribution = dist
            return dist

    def normal_variate(self, m: float, var: float, n: int):
        '''
        normal_variate returns random normal distribution variates 
        given that the variance parameter is greater than zero
        
        :float m: mean parameter mu
        :float var: variance parameter sigma squared
        :int n: number of variates to generate
        '''
        self.set_n(n)
        var = self.check_if_greater_than_zero(var)

        if self.n == 1:
            u = random()
            v = random()
            return m + (var**(1/2))*(((-2*log(u))**(1/2))*cos(2*pi*v))
        else:
            dist = []
            for n in range(0,self.n):
                u = random()
                v = random()
                dist.append(m + (var**(1/2))*(((-2*log(u))**(1/2))*cos(2*pi*v)))
            self.distribution = dist
            return dist

    def triang_variate(self, low: float, mode: float, high: float, n: int):
        '''
        triang_variate returns random triangular distribution variates 
        
        :float low: low bound value
        :float mode: most commonly occuring value, or 'peak' of 'triangle'
        :float high: high bound value
        :int n: number of variates to generate
        '''
        self.set_n(n)

        c = (mode - low)/(high - low)
        if self.n == 1:
            u = random()
            if u < c:
                return low + (u*(high - low)*(mode - low))**(1/2)
            elif u >= c:
                return high - ((1 - u)*(high - low)*(high - mode))**(1/2)
        else:
            dist = []
            for n in range(0,self.n):
                u = random()
                if u < c:
                    dist.append(low + (u*(high - low)*(mode - low))**(1/2))
                elif u >= c:
                    dist.append(high - ((1 - u)*(high - low)*(high - mode))**(1/2)) 
            self.distribution = dist
            return dist

    def weibull_variate(self, l: float, b: float, n: int):
        '''
        weibull_variate returns random weibull distribution variates
        given that both scale and shape parameters are greater than zero
        
        :float l: scale parameter lambda
        :float b: shape parameter beta
        :int n: number of variates to generate
        '''
        self.set_n(n)
        l = self.check_if_greater_than_zero(l)
        b = self.check_if_greater_than_zero(b)

        if self.n == 1:
            return (1/l)*(-log(random()))**(1/b)
        else:
            dist = []
            for n in range(0,self.n):
                dist.append((1/l)*(-log(random()))**(1/b))
            self.distribution = dist
            return dist

    def gamma_variate(self, a: float, b: float, n: int):
        '''
        gamma_variate returns random gamma distribution variates
        given that the shape and rate parameters are both greater than zero.
        separate algorithms are used depending on if shape parameter alpha is less than one,
        versus greater than or equal to one
        
        :float a: shape parameter alpha
        :float b: rate parameter beta
        :int n: number of variates to generate
        '''
        self.set_n(n)
        a = self.check_if_greater_than_zero(a)
        b = self.check_if_greater_than_zero(b)
        
        def recursive_gamma_1() -> float:
            '''
            recursive_gamma generates a random gamma distribution variate
            when shape parameter alpha is greater than or equal to one
            '''
            x = self.normal_variate(0, 1, 1)
            u = random()
            v = (1 + x/((9*d)**(1/2)))**3
            if v > 0:
                while log(u) >= 0.5*(x**2) + d - d*v + d*log(v):
                    return(recursive_gamma_1())
                return (d*v)/b
            else:
                return(recursive_gamma_1())
        

        def recursive_gamma_2() -> float:
                '''
                recursive_gamma generates a random gamma distribution variate
                when shape parameter alpha is less than one
                '''
                u = random()
                if u <= A/(A+B):
                    X = -2*log(1 - ((C*u)**(1/a))/2)
                else:
                    X = -log((C*(1 - u))/(a*(D**(a-1))))
                v = random()
                if X != 0:
                    if X <= D:
                        while v > ((X**(a - 1))*exp(-X/2))/((2**(a - 1))*((1-exp(-X/2))**(a - 1))):
                            return(recursive_gamma_2())
                        return X/b
                    else:
                        while v > (D/X)**(1 - a):
                            return(recursive_gamma_2())
                        return X/b
                else:
                    return(recursive_gamma_2())
                
        if a >= 1:
            d = a - (1/3)
            if self.n == 1:
                return(recursive_gamma_1())      
            else:
                dist = []
                for x in range(0,self.n):
                    dist.append(recursive_gamma_1())
                self.distribution = dist
                return dist
        else:
            D = 1.0334 - 0.0766*exp(2.2942*a)
            A = (2**a)*((1-exp(-D/2))**a)
            B = (a*(D**(a-1)))*exp(-D)
            C = A + B
            if self.n == 1:
                return(recursive_gamma_2())
            else:
                dist = []
                for x in range(0,self.n):
                    dist.append(recursive_gamma_2())
                self.distribution = dist
                return dist