# LUNA16 Data Analysis

This project explores lung nodule annotations and CT examples, extracts quantitative features from segmented nodules, and compares Random Forest and SVM classifiers. The radiomics notebook also contains PCA, K-means clustering, and an analysis of classification errors.

## Set up the environment

Install Git, Python 3.11, and a C compiler. The pinned PyRadiomics revision is built from source during installation. On macOS, install the Xcode Command Line Tools with `xcode-select --install` if needed. On Linux, use your distribution's C build tools. On Windows, install the Visual Studio Build Tools with the Desktop development with C++ workload.

```sh
git clone --branch final --single-branch https://github.com/ogumol/LUNA16DataAnalysis.git
cd LUNA16DataAnalysis
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python -m jupyter lab
```

On Windows PowerShell, use `py -3.11 -m venv .venv` and `.\.venv\Scripts\Activate.ps1` for the environment steps. Launch JupyterLab from the activated environment. If prompted for a kernel, select its Python kernel.

## Data and working directory

The clone includes the course dataset under [Description and Sample of the DataSet-20261006](Description%20and%20Sample%20of%20the%20DataSet-20261006/). It contains the annotation and nodule-voting Excel workbooks, sample full CT scans and masks under `CT/`, and cropped nodule images and masks under `VOIs/`. The image files use the `.nii.gz` format. Keep the folder names and hierarchy as checked out.

Open each notebook from the `notebooks/` folder in JupyterLab. Its kernel should start in that folder, so paths such as `../inspect_dataset.py` and `../results/` resolve from the checkout. If you are using another editor, set the kernel's working directory to `notebooks/`. Each notebook runs in its own kernel. Use **Restart Kernel and Run All Cells** to reproduce its results with a clean session. Running the notebooks regenerates files in `results/`, including some of the committed figures and tables.

## Run the analysis

| Notebook | What it runs |
| --- | --- |
| [01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb) | Checks the image/mask pairs, reads the annotation workbook, and summarizes nodule diameter and reader-assigned malignancy. |
| [01_data_exploration_extended.ipynb](notebooks/01_data_exploration_extended.ipynb) | Repeats the basic exploration, then uses the nodule-voting workbook for diagnosis summaries, morphology and texture comparisons, Spearman correlations, annotation agreement, and CT/VOI mask overlays. It writes five `eda_*.png` figures. |
| [Radiomics.ipynb](notebooks/Radiomics.ipynb) | Extracts radiomics features from segmented VOIs, derives the classification labels from reader assessments, evaluates patient-grouped classifiers, and generates PCA, clustering, model evaluation, and imaging figures. |

### Reproduce Radiomics with the saved feature table

To save time, open a copy of `Radiomics.ipynb` in the same `notebooks/` folder. In that copy, replace the bulk extraction cell beginning with `import logging` and containing `Images to process:` with this code. Keep the preceding setup and example cells, then restart and run all cells in order.

```python
radiomics_dataset = pd.read_csv(project_directory / "results" / "radiomics_features.csv")
```

For a complete run from the images, run the original notebook from top to bottom. The bulk extraction cell rebuilds `results/radiomics_features.csv` and reports any missing masks or failed extractions before the downstream analysis.

## Check the results

- [results/](results/) contains the committed figures and CSVs. Look for `eda_*.png` for the extended EDA, `pca_*.png` and `kmeans_*.png` for the unsupervised analysis, and `model_validation_comparison.csv` and the validation/test confusion matrices for model evaluation.
- The committed feature table contains 994 rows. The cleaned classification table contains 993 nodules, split into 595 training, 198 validation, and 200 test nodules. Check the patient-overlap counts in the split cell. All three counts should be zero.
- The extended EDA uses the 996 vote-derived nodule diagnoses in the voting workbook. The radiomics model uses labels derived from the annotation workbook and the available matched VOIs. Use the corresponding labels and counts when checking each notebook.
