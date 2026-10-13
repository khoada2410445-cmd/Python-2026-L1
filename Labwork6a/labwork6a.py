import os
import numpy as np
import matplotlib.pyplot as plt

# Generate 500 points in [-5, 5]
x = np.linspace(-5, 5, 500)

# Compute y = 2x + sin^2(x) + 3
y = 2 * x + (np.sin(x)) ** 2 + 3

# Plot figure
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y = 2x + \sin^2(x) + 3$', color='blue', linewidth=2)

plt.title("hello, po!", fontsize=14, fontweight='bold')
plt.xlabel("X axis", fontsize=12)
plt.ylabel("Y axis", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left')

# Save output to po.pdf
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(BASE_DIR, 'po.pdf')

plt.savefig(output_file, format='pdf', bbox_inches='tight')
plt.close()

print(f"[Labwork 6a] Output saved to {output_file}")