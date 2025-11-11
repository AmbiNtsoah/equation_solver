# 🎓 Equation Solver

## 🧮 Description

**Equation Solver** est une petite application Python avec interface graphique (PyQt5) qui permet de **résoudre les équations du second degré** de la forme :

\[
ax^2 + bx + c = 0
\]

L’application affiche :
- le **discriminant (Δ)**,  
- les **racines réelles** (x₁ et x₂),  
- ou un message si l’équation n’a **pas de solutions réelles**.

---

## 🧠 Fonctionnalités

- Entrée des coefficients `a`, `b` et `c` via l’interface graphique  
- Calcul automatique du discriminant  
- Affichage clair des racines réelles  
- Gestion des erreurs (valeurs invalides, a = 0, etc.)  
- Architecture respectant les principes **SOLID** et **Clean Code**

---

## Installation

- cloner le reposiory

```bash
git clone https://github.com/ton-nom-utilisateur/equation-solver.git
cd equation-solver
```

- installer pyqt5
```bash
pip install pyqt5
```

- lancer l'applicaion
```bash
python main.py
```