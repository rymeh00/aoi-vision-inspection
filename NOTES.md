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
