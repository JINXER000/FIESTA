import matplotlib.pyplot as plt;
import numpy as np;
import scipy.optimize as opt;

# This is the function we are trying to fit to the data.
def func(x, a, b, c):
     return a * np.exp(-b * x) + c

def f_1(x, A, B):
    return A * x + B
# Generate some data, you don't have to do this, as you already have your data
# xdata = np.linspace(0, 4, 50)
# y = func(xdata, 2.5, 1.3, 0.5)
# y_noise = 0.2 * np.random.normal(size=xdata.size)
# ydata = y + y_noise

xdata = np.array([16159.2, 17334.2, 16251.4, 22609, 1.38982e+06, 2.00012e+06, 5.02172e+06, 3.61781e+06, 4.3934e+06, 4.81698e+06, 5.81111e+06, 6.67861e+06, 7.482e+06, 9.93535e+06, 1.09539e+07, 1.26584e+07, 1.35077e+07])/7500000
ydata = [4, 5, 5, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7,  7, 7]
# Plot the actual data
plt.plot(xdata, ydata, ".")

x2 = np.array([2758.06, 2955.63, 18154.9, 18190, 15085.7, 1.20055e+06, 864335, 1.84234e+06, 4.87904e+06, 5.29839e+06, 6.7315e+06, 7.61749e+06, 9.17301e+06, 9.87764e+06, 1.11146e+07, 1.25104e+07, 1.37528e+07])/7500000
y2 = [1, 1, 2, 3, 36, 85, 97, 102, 88, 98, 119, 98, 123, 126, 132, 144, 137]
plt.plot(x2, y2,  ".", color="g")
# The actual curve fitting happens here
optimizedParameters, pcov = opt.curve_fit(f_1, xdata, ydata)

# Use the optimized parameters to plot the best fit
plt.plot(xdata, f_1(xdata, *optimizedParameters), label="ours")

optimizedParameters2, pcov2 = opt.curve_fit(f_1, x2, y2)

# Use the optimized parameters to plot the best fit
plt.plot(x2, f_1(x2, *optimizedParameters2), label="FIESTA")

plt.title('Mapping speed vs. Environmantal change')
plt.xlabel('Environmental change score')
plt.ylabel('ESDF construction time (ms)')
plt.legend()
# Show the graph
plt.legend()
plt.savefig("changerate.pdf")
plt.show()