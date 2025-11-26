import numpy as np
import matplotlib.pyplot as plt
# from tkinter import Tk
# from tkinter.filedialog import asksaveasfilename


# Define function 1
def f1(x):
    return np.sin(x)


# Define function 2
def f2(x):
    return np.cos(x)


# Define function 2
def f3(x, h):
    return (f1(x + h) - f1(x))/h


# Define function 3
def f4(x, h):
    return (f1(x + h/2) - f1(x - h/2))/h


# Define x-Values
xValues = np.linspace(-np.pi/2, np.pi/2, 10000)

# Calculate y-Values
yValues1 = f1(xValues)
yValues2 = f2(xValues)
yValues3_1 = f3(xValues, 5)
yValues3_2 = f3(xValues, 3)
yValues3_3 = f3(xValues, 1)
yValues3_4 = f3(xValues, 0.5)
yValues3_5 = f3(xValues, 0.01)
yValues4_1 = f4(xValues, 5)
yValues4_2 = f4(xValues, 3)
yValues4_3 = f4(xValues, 1)
yValues4_4 = f4(xValues, 0.5)
yValues4_5 = f4(xValues, 0.01)

###############################################################################
# Create plots, h = 5
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2,
         label=r"$f'(x) = \cos(x)$",
         linewidth=0.7)
plt.plot(xValues, yValues3_1,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues4_1,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 5')
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
    initialfile="exercise03-1.png"
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
# Create plots, h = 3
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2,
         label=r"$f'(x) = \cos(x)$",
         linewidth=0.7)
plt.plot(xValues, yValues3_2,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues4_2,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 3')
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
    initialfile="exercise03-2.png"
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
# Create plots, h = 1
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2,
         label=r"$f'(x) = \cos(x)$",
         linewidth=0.7)
plt.plot(xValues, yValues3_3,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues4_3,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 1')
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
    initialfile="exercise03-3.png"
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
# Create plots, h = 0.5
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2,
         label=r"$f'(x) = \cos(x)$",
         linewidth=0.7)
plt.plot(xValues, yValues3_4,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues4_4,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 0.5')
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
    initialfile="exercise03-4.png"
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
# Create plots, h = 0.01
plt.plot(xValues, yValues1,
         label=r'$f(x) = \sin(x)$',
         linewidth=0.7)
plt.plot(xValues, yValues2,
         label=r"$f'(x) = \cos(x)$",
         linewidth=0.7)
plt.plot(xValues, yValues3_5,
         label=r'$g(x) = \frac{\sin(x + h) - \sin(x)}{h}$',
         linewidth=0.7)
plt.plot(xValues, yValues4_5,
         label=r'$h(x) = \frac{\sin(x + \frac{h}{2}) - '
         r'\sin(x - \frac{h}{2})}{h}$',
         linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Annäherung der Ableitung, h = 0.01')
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
    initialfile="exercise03-5.png"
)

if location:
    plt.savefig(location, dpi=300)
    print(f"Plot gespeichert unter: {location}")
else:
    print("Speichern abgebrochen.")
"""

# Show plot
plt.show()
