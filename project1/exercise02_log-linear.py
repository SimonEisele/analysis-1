import numpy as np
import matplotlib.pyplot as plt
# from tkinter import Tk
# from tkinter.filedialog import asksaveasfilename


# Define function
def f(x):
    return 3 * (x**2)


# Define x-Values
xValues = np.linspace(1e-4, 10, 10000)

# Calculate y-Values
yValues = f(xValues)

# Calculate u-Values for linear plot (log10 transform)
uValues = np.log10(xValues)

###############################################################################
# Create plot log-linear (semilogx)
plt.semilogx(xValues, yValues, label=r'$f(x) = 3x^2$', linewidth=0.7)
plt.xlim(xValues.min(), xValues.max())
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Darstellung eines Graphen (log-linear) mit semilogx()')
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.8)
plt.grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.legend()

# Save plot as png
"""
root = Tk()
root.withdraw()

# Open explorer
location = asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    title="Speicherort für Plot auswählen",
    initialfile="exercise02-log-linear-semilogx.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")
"""

# Show plot
plt.show()

###############################################################################
# Create plot log-linear (plot)
plt.plot(uValues, yValues, label=r'$f(x) = 3x^2$', linewidth=0.7)
plt.xlim(uValues.min(), uValues.max())
plt.xlabel(r'$u = log_{10}(x)$')
plt.ylabel('f(x)')
plt.title('Darstellung eines Graphen (log-linear) mit plot()')
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.8)
plt.grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.legend()

# Save plot as png
"""
root = Tk()
root.withdraw()

# Open explorer
location = asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    title="Speicherort für Plot auswählen",
    initialfile="exercise02-log-linear-plot.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")
"""

# Show plot
plt.show()
