import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data (in MWh)
data = {
    "Model": ["GPT-3", "GPT-4", "GPT-5", "GPT-6"],
    "Training Energy (MWh)": [1287, 57000, 65000, 90000],   # midpoint estimates
    "Inference Energy (per 1M queries, MWh)": [75, 800, 1000, 1250]
}

df = pd.DataFrame(data)

# Melt data for seaborn grouped bar plot
df_melted = df.melt(
    id_vars="Model",
    value_vars=["Training Energy (MWh)", "Inference Energy (per 1M queries, MWh)"],
    var_name="Type",
    value_name="Energy (MWh)"
)

# Seaborn style
sns.set(style="whitegrid", context="talk")

# Create bar plot
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=df_melted, x="Model", y="Energy (MWh)", hue="Type", palette="Set2")

# Customize labels, title, scale
plt.title("Estimated Energy Consumption of GPT Models (Training vs Inference)", fontsize=16, weight='bold')
plt.ylabel("Energy (MWh)")
plt.xlabel("Model")
plt.yscale("log")

# Move legend BELOW the plot
plt.legend(
    title="Energy Type",
    loc="upper center",
    bbox_to_anchor=(0.5, -0.15),  # x=0.5 centers horizontally, y<0 moves below
    ncol=2,  # place legend items side by side
    frameon=False
)

# Add labels to bars
for container in plt.gca().containers:
    plt.bar_label(container, fmt="%.0f", label_type="edge", fontsize=9)

plt.tight_layout()

# Save figure as PDF
plt.savefig("gpt_energy_comparison.pdf", format="pdf", dpi=300, bbox_inches="tight")

# Show on screen
plt.show()
