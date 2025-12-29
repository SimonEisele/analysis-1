import numpy as np
import matplotlib.pyplot as plt
# from tkinter import Tk
# from tkinter.filedialog import asksaveasfilename


# Define function
def f(x):
    return np.sin(1/x)/(1/x)


# Define x-Values
xValues = np.linspace(1e-9, 10, 1000000)

# Calculate y-Values
yValues = f(xValues)

###############################################################################
# Create plot
plt.axhline(y=1,
            label=r'$y = 1$',
            color='r', linestyle='--', linewidth=0.7)
plt.plot(xValues, yValues,
         label=r'$f(x) = \frac{\sin(\frac{1}{x})}{\frac{1}{x}}$',
         linewidth=0.7)
plt.xlim(xValues.min(), xValues.max())
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Beispiel eines Grenzwerts')
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
