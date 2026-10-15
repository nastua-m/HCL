import matplotlib.pyplot as plt
import numpy as np

# Input sizes
sizes = ["50k", "500k", "5m", "50m", "500m"]
x = np.arange(len(sizes))

# Execution times
cpu = [0.15, 1.65, 17.56, 157.00, 346.70]

gpu_1024 = [0.15, 0.18, 0.30, 1.17, 11.50]
gpu_512 = [0.09, 0.19, 0.27, 1.16, 11.86]
gpu_32 = [0.16, 0.19, 0.22, 1.17, 11.28]

# Create plot
plt.figure(figsize=(10, 6))

plt.plot(sizes, cpu, marker="o", linewidth=2, label="CPU")
plt.plot(sizes, gpu_1024, marker="s", linewidth=2,
         label="GPU (1024 threads/block)")
plt.plot(sizes, gpu_512, marker="^", linewidth=2,
         label="GPU (512 threads/block)")
plt.plot(sizes, gpu_32, marker="D", linewidth=2,
         label="GPU (32 threads/block)")

# Logarithmic scale
plt.yscale("log")

# Labels and title
plt.xlabel("Input Size", fontsize=12)
plt.ylabel("Execution Time", fontsize=12)
plt.title("CPU vs GPU Execution Time", fontsize=14)

# Formatting
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

# Display plot
plt.show()
