# Fantastic Joules: Router Energy Demand Reproduction Project
**Computer Networks Course Project | Instructor: Sir Akmal**

This repository contains the software artifacts, analysis data, and final outputs generated for our semester reproduction project based on the IMC 2025 research paper:
> **"Fantastic Joules and Where to Find Them: Modeling and Optimizing Router Energy Demand"**  
> *ACM Internet Measurement Conference (IMC 2025)*  
> *Authors: Romain Jacob, Lukas Röllin, et al. | ETH Zurich*

---

## 👥 Team Members & Roles
* **M. Umair (Paper Lead)**: Summarized research methodology, claims, and coordinated team milestones.
* **Umair Bloch (Setup Lead)**: Configured environment, resolved Python/package dependencies.
* **Ahmad (Experiments Lead)**: Ran analysis notebooks and managed target figure generations.
* **Karar (Analysis Lead)**: Conducted comparative verification of reproduced figures vs. paper originals.

---

## 📂 Project Directory Structure

```
Fantastic-Joules-and-Where-to-Find-Them/
├── custom_workspace/          # High-resolution crops extracted from the paper PDF
│   ├── figure_4.png           # 3-way validation chart (Autopower vs. PSU vs. Model)
│   └── figure_9.png           # Router model validation chart
├── input/                     # Original CSV datasets (switch SNMP & datasheet specs)
├── output/                    # Generated output figures in PDF format
│   ├── 2025_IMC/figures/      # Original paper outputs (Figure 1, standard curves)
│   └── online/figures/        # Updated v2 outputs (including interpolation fixes)
├── datasheet-analysis_IMC25.ipynb       # Jupyter Notebook for Figure 1 & Table 1
├── PSU-efficiency-analysis_IMC25.ipynb  # Jupyter Notebook for base PSU efficiency
├── PSU-efficiency-analysis_v2.ipynb     # Jupyter Notebook for updated PSU efficiency
├── requirements.txt           # Python dependency lists
├── ENV.yml                    # Conda environment definition
├── run_all.py                 # Simulation runner to run notebooks sequentially
├── Final submission file.pdf  # Project PDF report
└── README.md                  # Project documentation (this file)
```

---

## ⚙️ How to Set Up & Run

To reproduce the analysis and plots, follow these steps:

### 1. Environment Setup
Make sure you have Python 3.8+ installed. Navigate to the project root directory and install dependencies:
```bash
# Create a Python virtual environment (optional but recommended)
python -m venv venv
# Activate the environment (Windows)
venv\Scripts\activate
# Activate the environment (Mac/Linux)
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt
pip install scipy docx
```

### 2. Execution
You can run the analysis in two ways:

* **Simulate via Python Script**:
  Run `run_all.py` to execute both the datasheet analysis and the base PSU efficiency notebooks programmatically:
  ```bash
  python run_all.py
  ```
* **Run Jupyter Notebooks (Manual)**:
  Open the Jupyter notebook interface:
  ```bash
  jupyter notebook
  ```
  Open and run the cells in:
  1. `datasheet-analysis_IMC25.ipynb`
  2. `PSU-efficiency-analysis_IMC25.ipynb`
  3. `PSU-efficiency-analysis_v2.ipynb`

---

## 📊 Key Reproduced Results

1. **Figure 1 (Total Power & Traffic)**: Successfully reproduced as `totalPowerTraffic.pdf` inside `output/2025_IMC/figures/`. It confirms that router power consumption remains highly static and does not correlate with traffic spikes.
2. **Table 1 (Typical Datasheet vs. Measured Median)**: Extracted median measured power metrics for all 8 routers. It validated the core claim of datasheet overestimations and the massive -44% underestimation for the Cisco 8201-24H8FH.
3. **Figure 4 & 9 (Validation Workaround)**: Because the authors omitted raw SNMP and Autopower validation time-series data for individual routers in the public archive, we programmatically extracted these figures in high definition directly from pages 8 and 15 of the original research PDF and saved them to the `custom_workspace/` directory.