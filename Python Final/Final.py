import numpy as np
import matplotlib.pyplot as plt

# This section defines the constants L, hbar, and m.
L = 1.0  # the length of the region
hbar = 1.0545718e-34  # Reduced Planck's constant. (planck's constant over 2 pi).
m = 9.10938356e-31  # Mass of an electron.

# This section defines the neccesary function for the given problem such as the solutions to the Shrodinger Equation. 
# wave funtion is the solution to the shrodinger equation for infinite square box in one spacial dimention. 
def wavefunction(x, n, L):
    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

# Create position array
x = np.linspace(0, L, 1000)  # Position array
n_values = [1]  # this is the quantum number, which assigns the energy level of the electron. 1 means ground energy. 

# Calculate wavefunction and probability density for the initial state
#probability density is the square of the absolute value of the wave equation. 
psi_total = np.zeros_like(x, dtype=complex)
for n in n_values:
    psi_total += wavefunction(x, n, L)
prob_density = np.abs(psi_total)**2

# Create the figure and axes for plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 12))
ax[0].set_xlim(0, L)
ax[0].set_ylim(-2.5, 2.5)  # Set Y limits as specified
ax[1].set_xlim(0, L)
ax[1].set_ylim(0, 2.3)  # Set Y limits as specified

# Plot wavefunction and probability density
ax[0].plot(x, np.real(psi_total), lw=2, color='red')
ax[1].plot(x, prob_density, lw=2, color='red')

#gridlines
ax[0].grid(True, which='both', color='lightblue', linestyle='-', linewidth=0.7)
ax[1].grid(True, which='both', color='lightblue', linestyle='-', linewidth=0.7)
ax[0].minorticks_on()
ax[1].minorticks_on()
ax[0].set_aspect(aspect='auto')
ax[1].set_aspect(aspect='auto')

# Plot labels and titles
ax[0].set_xlabel('Position (x)')
ax[0].set_ylabel('Wavefunction')
ax[0].set_title('Wavefunction')
ax[1].set_xlabel('Position (x)')
ax[1].set_ylabel('Probability Density')
ax[1].set_title('Probability Density')

# Adjust layout for better appearance
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the tight layout to give space for the title
plt.show()
