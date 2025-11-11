import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


# Define function 1
def f1(x):
    return np.sin(x)


# Define function 2
def f2(x, h):
    return (f1(x + h) - f1(x))/h


# Define function 2
def f3(x, h):
    return (f1(x + h/2) - f1(x - h/2))/h


# Define x-Values
xValues = np.linspace(-np.pi/2, np.pi/2, 10000)

# Calculate y-Values
yValues1 = f1(xValues)
yValues2_1 = f2(xValues, 0.8)
yValues2_2 = f2(xValues, 0.4)
yValues2_3 = f2(xValues, 0.2)
yValues2_4 = f2(xValues, 0.1)
yValues2_5 = f2(xValues, 0.01)
yValues3_1 = f3(xValues, 0.8)
yValues3_2 = f3(xValues, 0.4)
yValues3_3 = f3(xValues, 0.2)
yValues3_4 = f3(xValues, 0.1)
yValues3_5 = f3(xValues, 0.01)

###############################################################################
# Create plots, h = 0.8
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2_1,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues3_1,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 0.8')
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
    initialfile="exercise03-1.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()

###############################################################################
# Create plots, h = 0.4
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2_2,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues3_2,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 0.4')
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
    initialfile="exercise03-2.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()

###############################################################################
# Create plots, h = 0.2
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2_3,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues3_3,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 0.2')
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
    initialfile="exercise03-3.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()

###############################################################################
# Create plots, h = 0.1
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2_4,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues3_4,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 0.1')
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
    initialfile="exercise03-4.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()

###############################################################################
# Create plots, h = 0.01
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2_5,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues3_5,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 0.01')
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
    initialfile="exercise03-5.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")

# Show plot
plt.show()
