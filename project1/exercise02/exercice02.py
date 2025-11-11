import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


# Define function
def f(x):
    return 3 * (x**3)


# Define x-Values
xValues = np.linspace(1e-9, 10, 10000)

# Calculate y-Values
yValues = f(xValues)

###############################################################################
# Create plot linear-linear
plt.plot(xValues, yValues,
         label=r'$f(x) = 3x^3$',
         linewidth=0.7)
plt.xlim(0, 10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Lineare Darstellung eines Graphen')
plt.grid(which='both', linestyle='--', linewidth=0.6)
plt.minorticks_on()
plt.legend()

# Save plot as png
root = Tk()
root.withdraw()

# Open explorer
location = asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    title="Speicherort für Plot auswählen",
    initialfile="exercise02-linear-linear.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()

###############################################################################
# Create plot log-linear
plt.semilogx(xValues, yValues, label=r'$f(x) = 3x^3$', linewidth=0.7)
plt.xlim(1e-9, 10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Darstellung des Graphen mit linearer X- und Y-Achse')
plt.grid(which='major', linestyle='--', linewidth=0.6)
plt.grid(which='minor', linestyle='--', linewidth=0.4)
plt.minorticks_on()
plt.legend()

# Save plot as png
root = Tk()
root.withdraw()

# Open explorer
location = asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    title="Speicherort für Plot auswählen",
    initialfile="exercise02-log-linear.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()

###############################################################################
# Create plot linear-log
plt.semilogy(xValues, yValues, label=r'$f(x) = 3x^3$', linewidth=0.7)
plt.xlim(1e-9, 10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Darstellung des Graphen mit logarithmischer Y-Achse')
plt.grid(which='major', linestyle='--', linewidth=0.6)
plt.grid(which='minor', linestyle='--', linewidth=0.4)
plt.minorticks_on()
plt.legend()

# Save plot as png
root = Tk()
root.withdraw()

# Open explorer
location = asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    title="Speicherort für Plot auswählen",
    initialfile="exercise02-linear-log.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()

###############################################################################
# Create plot log-log
plt.loglog(xValues, yValues, label=r'$f(x) = 3x^3$', linewidth=0.7)
plt.xlim(1e-9, 10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Darstellung des Graphen mit logarithmischer X- und Y-Achse')
plt.grid(which='major', linestyle='--', linewidth=0.6)
plt.grid(which='minor', linestyle='--', linewidth=0.4)
plt.minorticks_on()
plt.legend()

# Save plot as png
root = Tk()
root.withdraw()

# Open explorer
location = asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    title="Speicherort für Plot auswählen",
    initialfile="exercise02-log-log.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()
