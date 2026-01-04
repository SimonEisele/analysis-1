import numpy as np
import matplotlib.pyplot as plt
# from tkinter import Tk
# from tkinter.filedialog import asksaveasfilename


# Define function
def f(x):
    return x / (1 + x)


# Define x-Values
xValues = np.linspace(10e-4, 1000, 1000000)

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
plt.semilogx(xValues, yValues,
             label=r'$u(r) = \frac{r}{(1 + r)}$',
             linewidth=0.7)
plt.xlim(xValues.min(), xValues.max())
plt.xlabel('r')
plt.ylabel('u(r)')
# plt.title('Leistung einer Spannungsquelle in Funktion des Lastwiderstands')
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
    initialfile="exercise01.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")
"""

# Show plot
plt.show()
