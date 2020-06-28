import numpy as np
import matplotlib.pyplot as plt

def xj_lambda(xj, lmd):
    # Equation 4-34
    if lmd == 0:
        return np.log(xj)
    else:
        return (xj ** lmd - 1) / lmd


def x_lambda(x, lmd):
    # Equation 4-36
    s = 0
    for xj in x:
        s += xj_lambda(xj, lmd)
    return (s / len(x))


def l_lambda(x, lmd):
    # Equation 4-35
    n = len(x)
    l = 0
    # first_part: $-\frac{n}{2}\ln(\frac{1}{n}\sum_{j=1}^{n}(x_j^{(\lambda)}-\overbar{x_j^{(\lambda)}}))$
    # second_part: $(\lambda-1)\sum_{j=1}^{n}\ln x_j$
    xl = x_lambda(x, lmd)
    for xj in x:
        sub = xj_lambda(xj, lmd) - xl
        l += sub ** 2
    w = l / n
    first_part = (-n / 2) * np.log(w)
    second_part = (lmd - 1) * np.sum(np.log(x))
    return (first_part + second_part)

def plot_lambda(x, y):
    fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure and an axes.
    lstyle = '-*b'
    ax.plot(x, y, lstyle)
    ax.set_xlabel(r'$ \lambda $')  # Add an x-label to the axes.
    ax.set_ylabel(r'$ \mathcal{L(\lambda)} $')  # Add a y-label to the axes.
    ax.set_title(r'Plot of $\mathcal{L(\lambda)}$ versus $\lambda$')  # Add a title to the axes.
    i = y.index(max(y))
    A = [x[i]]
    B = [max(y)]
    plt.plot(A[0], B[0], 'ro')
    for xy in zip(A, B):  # <--
        ax.annotate('(%.2f, %.2f)' % xy, xy=xy, textcoords='data', xytext=(0,-1))
    fig.savefig('fig.pdf')
    fig.savefig('fig.png', dpi=500)
    plt.show()

if __name__ == "__main__":
    # Example 4-10
    x = [.15, .09, .18, .10, .05, .12, .08, .05, .08, .10, .07, .02, .01, .10,
         .10, .10, .02, .10, .01, .40, .10, .05, .03, .05, .15, .10, .15, .09,
         .08, .18, .10, .20, .11, .30, .02, .20, .20, .30, .30, .40, .30, .05]
    lmds = np.linspace(-5, 5, 1000)
    l_lambdas = []
    for lmd in lmds:
        l_lambdas.append(l_lambda(x, lmd))
        # print(round(lmd, 2), ':\t', l_lambda(x, lmd))
    plot_lambda(lmds, l_lambdas)