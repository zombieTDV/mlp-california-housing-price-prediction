import nbformat

notebook_path = 'notebooks/03_model_training.ipynb'

# Read the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Find and update the plotting cell
for cell in nb.cells:
    if cell.cell_type == 'code' and 'plt.plot(losses' in cell.source:
        new_source = """plt.figure(figsize=(12, 7))
plt.plot(losses, label='Training Loss', color='#1f77b4', linewidth=2)

# Mark the minimum loss point
min_loss = min(losses)
min_epoch = losses.index(min_loss)
plt.scatter(min_epoch, min_loss, color='red', zorder=5, s=50, label=f'Min Loss ({min_loss:.4f} at Epoch {min_epoch})')

# Add annotations for clarity
plt.annotate(f'Initial Loss: {losses[0]:.4f}', xy=(0, losses[0]), xytext=(epochs*0.05, losses[0]),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.title(f"Training Process (Learning Rate = {learning_rate})", fontsize=14, fontweight='bold')
plt.xlabel("Epoch", fontsize=12)
plt.ylabel("MSE Loss", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Quick evaluation
print(f"Initial Loss: {losses[0]:.4f}")
print(f"Final Loss: {losses[-1]:.4f}")
if losses[-1] < losses[0]:
    print("Evaluation: Model is LEARNING well (Loss is decreasing).")
else:
    print("Evaluation: Model is NOT LEARNING (Loss is not decreasing). Please check the code or Learning Rate.")"""
        cell.source = new_source
        print("Updated plotting cell.")

# Write back
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print("Saved notebook.")
