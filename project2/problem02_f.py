import numpy as np
import matplotlib.pyplot as plt


# Define function
def f(x):
    return np.cos(2 * np.pow(x, 3) + 1) * np.exp(x - 1)


# Define x-Values
xValues = np.linspace(-2.5, 2.5, 1000000)

# Calculate y-Values
yValues = f(xValues)

###############################################################################
# Plot-parameters
plt.rcParams.update({
        "axes.labelsize": 18,      # Achsenbeschriftungen
        "legend.fontsize": 18,     # Legende
        "xtick.labelsize": 18,     # Tick-Beschriftungen X
        "ytick.labelsize": 18      # Tick-Beschriftungen Y
    })

# Create plot
plt.plot(xValues, yValues, label=r'$f(x)$', linewidth=0.7)
plt.xlim(xValues.min(), xValues.max())
plt.xlabel('x')
plt.ylabel('f(x)')
# plt.title('Leistung einer Spannungsquelle in Funktion des Lastwiderstands')
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.8)
plt.grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.legend()

# Show plot
plt.show()
