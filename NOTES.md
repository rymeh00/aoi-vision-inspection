Build Journal — AOI Vision Inspection

My day-by-day log, in my own words. Purpose: (1) make sure I truly understand what I did, (2) prepare my interview answers, (3) prove honest, dated work.

Day 1 — Environment setup — Date: 16 / 09 / 2026 :

1. Installed Python 3.11.9 — the programming language of this project.
Key detail: ticked "Add python.exe to PATH" → PATH = the list of foldersWindows searches when I type a command. Without it: 'python' is not recognized.

2. Installed Git and VS Code, then introduced myself to Git(git config --global user.name / user.email).

3. Created a GitHub account and a public repository aoi-vision-inspection.
  * Git = tool on my PC that saves snapshots of my code ("commits").
  * GitHub = website that hosts those snapshots online (public).

4. Cloned the repo to Documents (git clone) → my local folder is now linked to the online copy (called origin).

5. Created a virtual environment: python -m venv venv, then venv\Scripts\activate.
   * A venv = a private Python toolbox for this project only, so its libraries never clash with other projects. Created ONCE; activated at every session(prompt must start with (venv)).

6. Installed the libraries (pip install opencv-python numpy pandas matplotlib scikit-learn streamlit plotly) and saved the exact list:pip freeze > requirements.txt → anyone can recreate my setup with pip install -r requirements.txt.

7. Created the project structure in VS Code: NOTES.md, .gitignore, src/, reports/.
   * .gitignore is a config file: I never "run" it. Git reads it automaticallyand ignores venv/, data/, models/. (Proof: git status never showed venv.)

8. Wrote and ran my first program — app.py with Streamlit, visible in mybrowser at localhost:8501.
   * localhost = a page served by my own computer. The terminal running streamlit run app.py IS the server → it must stay open.

9. Saved my work: git add . → git commit -m "Day 1: ..." → git push. 
    * Verified on GitHub: commit de088ef, "5 minutes ago". Local save → online copy.

Day 2 — First real data, first real debugging — Date: 17 / 09 / 2026

1. Downloaded the MVTec AD metal_nut dataset from the official site(mvtec.com) → moved metal_nut.tar.xz into the project folder → mkdir data.

2. Unpacked and verified the structure: train / test / ground_truth.

3. Wrote and ran src/explore.py: auto-discovers categories from the folders(never hardcode what you can measure), counts images, displays one sample per category.
   * Import libraries : 3 toolboxes: Path (addresses), cv2 (images),plt (display)
   * Build the address : data_dir = Path("data") / "metal_nut" : Smart path object pointing at the dataset
   * Safety check: if not data_dir.exists(): raise SystemExit(...) : If the folder is missing → stop immediately with a clear message (fail fast, fail clear)
   * Auto-discover categories : List the folders inside test/, keep only folders, take names, sort A→Z → ['bent','color','flip','good','scratch']
   * Count per category : Dictionary: category name → number of images. Measured, not assumed.
   * Count training images : The 220 — our detector's future food
   * Size the grid : Ceiling division: 5 categories → 2 rows. 
   * Display a sample of each category

Summary : The script verifies the dataset exists, auto-discovers its categories from the folder structure, measures the image count per category, then deterministically displays one grayscale sample of each category in a grid — always looking at data before writing any detection logic