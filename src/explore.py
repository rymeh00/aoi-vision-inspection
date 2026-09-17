"""Day 2 — Explore the MVTec AD 'metal_nut' dataset.

Rule #1 of vision engineering: LOOK at your data before coding logic.
This script verifies the folder structure, COUNTS images per category
(measured, not assumed!), and displays one sample of each category.
"""

from pathlib import Path
import cv2
import matplotlib.pyplot as plt


def main():
    data_dir = Path("data") / "metal_nut"
    if not data_dir.exists():
        raise SystemExit(f"Folder not found: {data_dir} — check the extraction step!")

    test_dir = data_dir / "test"
    print("Inside metal_nut:", 
    sorted(p.name for p in data_dir.iterdir()))

    # --- 1) AUTO-DISCOVER categories (never hardcode what you can measure) ---
    categories = sorted(p.name for p in test_dir.iterdir() if p.is_dir())
    print("Categories found:", categories)

    # --- 2) MEASURE: count images per category ---
    counts = {}
    for cat in categories:
        counts[cat] = len(list((test_dir / cat).glob("*.png")))
        print(f"  test/{cat:10s}: {counts[cat]:4d} images")

    train_count = len(list((data_dir / "train" / "good").glob("*.png")))
    print(f"  train/good     : {train_count:4d} images")

    # --- 3) One sample per category, in a grid sized to fit ---
    ncols = 3
    nrows = (len(categories) + ncols - 1) // ncols   # ceil division
    fig, axes = plt.subplots(nrows, ncols, figsize=(4 * ncols, 4 * nrows),
                             squeeze=False)
    axes = axes.ravel()          # flatten the 2D grid of panels into a line
    fig.suptitle("metal_nut — one sample per category")

    for i, cat in enumerate(categories):
        first_image = sorted((test_dir / cat).glob("*.png"))[0]
        image = cv2.imread(str(first_image), cv2.IMREAD_GRAYSCALE)
        axes[i].imshow(image, cmap="gray")
        axes[i].set_title(f"{cat} ({counts[cat]} images)")
        axes[i].axis("off")

    for ax in axes[len(categories):]:   # hide unused panels
        ax.axis("off")

    plt.tight_layout()
    plt.show()   # CLOSE the window to let the script finish


if __name__ == "__main__":
    main()