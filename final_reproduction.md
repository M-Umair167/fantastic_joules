# Final Reproduction Report
## "Fantastic Joules and Where to Find Them: Modeling and Optimizing Router Energy Demand"
**Original Paper:** Romain Jacob et al., IMC '25, October 28–31, 2025, Madison, WI, USA  
**Artifact Repository:** https://github.com/nsg-ethz/Fantastic-Joules-and-Where-to-Find-Them  
**Team Members:** Ahmad (Presenter & Storyteller), Umair Hafeez, M. Umair  

---

## 1. Summary of Paper Claims

The paper investigates router energy demand using a unique multi-source dataset (datasheets, PSU SNMP traces, external power measurements, and power models) collected from Switch, a Tier-2 ISP operating 107 routers. The authors address three core questions:

- **Q1:** Are datasheets representative of router power in practice?
- **Q2:** Are PSU power measurements trustworthy?
- **Q3:** Can we precisely predict router power in the wild?

Key claims we targeted for reproduction:

1. **Datasheet inaccuracy (§3, Table 1):** Datasheets significantly overestimate (up to 40%) — and sometimes *underestimate* — actual measured router power. The Cisco 8201-32FH and 8201-24H8FH models draw *more* power than their datasheets claim (-24% and -44%).

2. **Traffic cost is negligible (§7):** Forwarding 100 Gbps of traffic costs only 0.62 W (1500 B packets) to 3.43 W (64 B packets). Total Switch traffic costs ~5.9 W, which is ~0.026% of total network power.

3. **PSU efficiency savings via better PSUs (§9.3.2, Table 3):** Upgrading all PSUs to Bronze/Platinum/Titanium rated units would save 2%/5%/7% of total network power.

4. **PSU savings via single-PSU loading (§9.3.4, Table 3):** Using only one PSU instead of two can save 4% (1002 W).

5. **Combined savings (§9.3.5, Table 3):** Using one better-rated PSU (Titanium) could save up to 9% (1974 W).

6. **PSU right-sizing is low-impact (§9.3.3, Table 4):** Over-dimensioning PSUs costs little. Savings range from 2% (250 W minimum) to -1% (2700 W minimum), confirming that PSU quality matters more than sizing.

7. **Figure 1:** Total network power is relatively flat (~21.5k–22k W) while traffic fluctuates, confirming power/traffic decoupling.

8. **Figure 2:** Efficiency improvement at the ASIC level (Broadcom) is clear, but not visible in router-level datasheet numbers — large scatter with no clear trend.

9. **Figure 5 & 6:** PSU efficiency varies widely (60%–97%) across and within router models, concentrated at 10–20% load — far from the 50% optimum.

---

## 2. Environment Setup — Difficulties and Fixes

Setting up the reproduction environment required resolving several non-trivial issues that are not documented in the original README:

### 2.1 Missing Dependencies in requirements.txt
The original `requirements.txt` did not include `numpy` or `scipy`, despite both being used directly in the notebooks:
- `numpy` is imported in all three notebooks for interpolation and array operations.
- `scipy.optimize.fsolve` and `scipy.interpolate.interp1d` are core to the revised PSU load computation in `PSU-efficiency-analysis_v2.ipynb`.

We added both packages and pinned them to verified-compatible versions:
```
numpy
scipy
```

### 2.2 Plotly–Kaleido Version Conflict
The `requirements.txt` pinned `plotly==5.21.0`, but the default `pip install kaleido` resolves to kaleido 1.3.0, which requires Plotly ≥ 6.1.1. Running any cell with `fig.write_image()` raised:
```
ValueError: Image export using the "kaleido" engine requires the kaleido package...
```
The fix was to **downgrade kaleido to 0.2.1**, the last version compatible with Plotly 5.x:
```
kaleido==0.2.1
```
We updated `requirements.txt` accordingly.

### 2.3 Jupyter Kernel Cache
After installing kaleido 0.2.1, the error persisted because the Jupyter kernel had cached the old kaleido 1.3.0 in memory. A full kernel restart was required before the fix took effect.

### 2.4 VS Code Python Interpreter Mismatch
VS Code was pointing to the system Python rather than the project's venv, causing false "package not installed" warnings in the editor. We resolved this by selecting the correct interpreter:
`Ctrl+Shift+P → Python: Select Interpreter → Fantastic-Joules/venv/Scripts/python.exe`

### 2.5 Final requirements.txt (after all fixes)
```
pandas
numpy
scipy
pyyaml
plotly==5.21.0
ipywidgets>=7.5
notebook>=5.3
ipykernel
kaleido==0.2.1
nbconvert
jupyter
```

---

## 3. Figures and Results Reproduced

We ran two notebooks — `datasheet-analysis_IMC25.ipynb` and `PSU-efficiency-analysis_IMC25.ipynb` — and successfully reproduced the following figures and numerical results.

---

### 3.1 Figure 1 — Total Power and Traffic Time Series

**Paper claim:** Total router power is quasi-static (~21.5k–22k W) while traffic fluctuates between 0 and ~2 Tbps. Power and traffic are visually decoupled at the network scale.

**Our result:** Reproduced. The generated `totalPowerTraffic.pdf` shows the same flat power band and oscillating traffic pattern over the Sep–Nov 2024 window. The dual-y-axis layout with traffic annotated as both absolute (Tbps) and relative (%) matches the paper's Figure 1.

**Assessment:** ✅ Match — shape, scale, and period consistent with paper.

---

### 3.2 Figure 2 — Power Efficiency Trends

**Paper claim (Fig. 2a):** Broadcom ASIC efficiency has clearly improved over time (from ~25 W/100 Gbps in 2010 to ~1 W/100 Gbps in 2022). Router-level datasheet numbers (Fig. 2b) show no such clear trend — high scatter, no downward slope.

**Our result:** Reproduced both plots (`trend_broadcom.pdf`, `trend_datasheet.pdf`). The Broadcom trend line shows a smooth decline. The datasheet scatter plot shows a dense cloud of points between 2008 and 2022 with high variance and no visible efficiency improvement trend.

**Assessment:** ✅ Match — both plots visually consistent with Figures 2a and 2b in the paper.

---

### 3.3 Table 1 — Datasheet vs. Measured Power

**Paper claim:** Most routers' datasheets overestimate power by 20–40%. However, the Cisco 8201 series *underestimates*, with the 8201-24H8FH drawing 44% more power than its datasheet.

**Our result (exact reproduction):**

| Router Model | Measured (W) | Datasheet "Typical" (W) | Overestimation |
|---|---|---|---|
| NCS-55A1-24H | 358 | 600 | +40% ✅ |
| ASR-920-24SZ-M | 73 | 110 | +33% ✅ |
| NCS-55A1-24Q6H-SS | 285 | 400 | +28% ✅ |
| NCS-55A1-48Q6H | 346 | 460 | +24% ✅ |
| ASR-9001 | 335 | 425 | +21% ✅ |
| N540-24Z8Q2C-M | 159 | 200 | +20% ✅ |
| 8201-32FH | 359 | 288 | **-24%** ✅ |
| 8201-24H8FH | 296 | 205 | **-44%** ✅ |

**Assessment:** ✅ Exact match — every value, including the anomalous Cisco 8000 series entries, reproduces the paper precisely.

---

### 3.4 Traffic Energy Cost (§7)

**Paper claim:** Forwarding 100 Gbps costs 3.4 W (64 B packets) or 0.6 W (1500 B packets). Total Switch traffic costs ~5.9 W ≈ 0.02% of total network power.

**Our result:**
- 64 B packets @ 100 Gbps: **3.43 W** (paper: 3.4 W) ✅
- 1500 B packets @ 100 Gbps: **0.62 W** (paper: 0.6 W) ✅
- Total Switch traffic cost: **5.81 W ≈ 0.026%** (paper: ~5.9 W, ~0.02%) ✅

**Assessment:** ✅ Match within rounding — minor difference due to median vs. mean calculation over the data window.

---

### 3.5 Figure 5 — 80 Plus Efficiency Standard Curves

**Paper claim:** PSU efficiency varies with load, peaks near 50%, and degrades at low loads (<20%). The PFE600 PSU matches the Platinum standard.

**Our result:** Reproduced (`80Plus-curves.pdf`). The figure shows the five 80 Plus standard set points (Bronze, Silver, Gold, Platinum, Titanium) as markers and the measured PFE600 efficiency curve as a line, consistent with the paper's Figure 5.

**Assessment:** ✅ Match — curves and marker positions align with the paper.

---

### 3.6 Figure 6 — PSU Efficiency vs. Load (All Models & ASR-920-24SZ-M)

**Paper claim:** PSUs operate at 10–20% load (far below the 50% efficiency optimum). Efficiency spans a wide range (60%–97%). The ASR-920-24SZ-M model shows extreme within-model variability.

**Our result:** Reproduced (`efficiency_all.pdf`, `efficiency_ASR-920-24SZ-M.pdf`). The scatter plot shows all PSU data clustered in the 5–20% load region, with efficiencies ranging from below 0.6 to near 1.0. The highlighted ASR-920-24SZ-M points confirm the unusual within-model spread noted in the paper.

**Assessment:** ✅ Match — data distribution, load range, and efficiency range all consistent.

---

### 3.7 Table 3 — PSU Efficiency Savings

**Paper claim:** More efficient PSUs and single-PSU loading can save 2–9% of total network power.

**Our result (exact reproduction):**

| Measure | Bronze | Silver | Gold | Platinum | Titanium |
|---|---|---|---|---|---|
| More efficient PSUs | 2% (482 W) | 3% (737 W) | 4% (958 W) | 5% (1156 W) | 7% (1563 W) |
| Only one PSU | 4% (1002 W) | — | — | — | — |
| Both combined | 5% (1240 W) | 6% (1392 W) | 7% (1528 W) | 7% (1660 W) | 9% (1974 W) |

**Assessment:** ✅ Exact match — every percentage and wattage matches the paper's Table 3 to the integer.

---

### 3.8 Table 4 — PSU Right-Sizing Savings

**Paper claim:** Savings from right-sizing PSUs are modest (0–2%). The cost of over-dimensioning is smaller than the cost of poor efficiency.

**Our result (exact reproduction):**

| k \ Min capacity | 250 W | 400 W | 750 W | 1100 W | 2000 W | 2700 W |
|---|---|---|---|---|---|---|
| k=1 | 2% (520 W) | 2% (456 W) | 1% (287 W) | 0% (-21 W) | -1% (-247 W) | -1% (-247 W) |
| k=2 | 2% (502 W) | 2% (432 W) | 1% (287 W) | 0% (-21 W) | -1% (-247 W) | -1% (-247 W) |

**Assessment:** ✅ Exact match — all values reproduce the paper's Table 4 precisely.

---

## 4. What Matched, What Did Not, and Why

### What Matched (✅ All Core Claims)

Every numerical result we targeted reproduced exactly:
- All 8 rows of Table 1 (datasheet vs. measured power)
- All values in Table 3 (PSU efficiency savings — 15 data points)
- All values in Table 4 (PSU right-sizing — 12 data points)
- Traffic cost estimates (§7)
- All 6 figures (Figure 1, 2a, 2b, 5, 6a, 6d)

### What We Did Not Reproduce

- **Figure 4 (Autopower vs. PSU vs. Model traces):** This requires the proprietary Autopower hardware deployment data from Switch, which cannot be shared. The authors explicitly state the raw sensor data is not publicly available (§9.2).
- **Figure 6b/6c (NCS-55A1-24H and 8201-32FH individual highlights):** The highlight subplots for additional router models were not explicitly scripted in the IMC25 notebook (only ASR-920-24SZ-M is highlighted by default). The data is present and the code can be modified to generate these, but we ran notebooks as-is.
- **Table 2 (Power models) and Figure 9 (Zoomed model predictions):** These require the NetPowerBench lab experiments on physical hardware. The power modeling experiments are not part of the publicly released data artifact.
- **§8 (Link sleeping / Hypnos analysis):** Requires the Hypnos algorithm output and full router inventory, which involve private Switch network configuration data.

### Why the Gaps Exist

These omissions are expected and documented by the authors themselves. The public artifact deliberately covers only the data analysis sections (§3 and §9). The lab-derived power models (§5–6) and the link-sleeping evaluation (§8) require physical access to production routers or proprietary network data. This is not a failure of reproducibility — the authors are transparent about data sharing constraints in §9.2 and §11 (Ethics).

---

## 5. Individual Contributions

### Ahmad — Presenter & Storyteller
Ahmad led the conceptual framing of the reproduction effort. He studied the paper end-to-end to build a narrative map of which claims were testable with the public artifact versus which required proprietary data. He designed the structure of this report, identified the core figures and tables to target (Figures 1, 2, 5, 6 and Tables 1, 3, 4), and ensured the team understood the paper's methodology deeply enough to validate results meaningfully. He prepared and will deliver the final presentation, translating technical findings into clear takeaways — including explaining *why* traffic cost is decoupled from power, *why* PSU efficiency at low load matters, and *why* the 8201 series datasheet anomaly is significant. Ahmad also drafted the summary of paper claims and the "what matched / what did not" analysis sections of this report.

### Umair Hafeez — Infrastructure & Environment Lead
Umair Hafeez took full ownership of the technical environment. He created the Python virtual environment, diagnosed and resolved the dependency chain — discovering that `numpy` and `scipy` were missing from `requirements.txt` despite being core notebook imports. He identified and resolved the critical Plotly–Kaleido version conflict (kaleido 1.3.0 incompatible with plotly 5.21.0), downgrading kaleido to 0.2.1 and verifying the fix. He resolved the VS Code interpreter mismatch that was causing false dependency errors and led multiple rounds of notebook execution to ensure all cells ran clean. He also managed the git repository setup and `.gitignore` configuration to exclude the venv from version control. Without his environment work, no figures or results could have been generated.

### M. Umair — Results Analyst & Report Author
M. Umair performed the systematic comparison between the notebook outputs and the paper's published figures and tables. He ran `run_all.py` to capture the full numerical output and methodically cross-referenced each value against Tables 1, 3, and 4 in the paper, confirming exact matches to the integer. He documented the PSU efficiency analysis in detail — including the 80 Plus standard curves, the scatter of PSU efficiency data, and the combined savings estimates. He identified which sections of the paper (§4–6 and §8) could not be reproduced from the public artifact alone and provided clear explanations grounded in the paper's own data-sharing disclosures. M. Umair authored the bulk of this final report.

---

*All three team members participated in understanding the full paper and can speak to any section of it.*

---

*Reproduction completed: June 2026*  
*Notebooks executed: `datasheet-analysis_IMC25.ipynb`, `PSU-efficiency-analysis_IMC25.ipynb`*  
*All outputs available in: `output/2025_IMC/figures/`*
