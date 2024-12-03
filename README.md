# Uniconf
This repository **Uniconf** contains:
1) The Uniconf computer program for conformational search/sampling in isolated molecules and molecular clusters
2) A few Python 3 scripts to prepare input files / analyse the Uniconf results (if needed)

## Prerequisites
1) Linux operational system (for Uniconf)
2) Python 3 (for scripts)

## Running the code
### Download the uniconf binary & copy it to your folder of choice
### Prepare your input files
There are two ways to generate the Uniconf programs input files:
1. Manual preparation with your editor of choice. Please, see some examples here: https://github.com/QuantumChemistryGroup/uniconf-bin/wiki
2. Running the Python 3 scripts on the ORCA or Priroda output files with charges (please, e-mail us if you need these scripts for other quantum chemistry programs). 
  - Prepare molecule.CHR file with charges:
    - ```python3 /path/to/your/script/get_CHR_ORCA.py molecule.out``` (for ORCA output molecule.out with CHELPG, HIRSHFELD or MULLIKEN charges)
  
    - ```python3 /path/to/your/script/get_CHR_PRIRODA.py molecule.out``` (for Priroda output molecule.out with HIRSHFELD charges) 
  - In case of rotatable bonds in your system, prepare molecule.ROT file. In this file each line should contain rotatable bond specification ```Atom1   Atom2   Angle_Increment   Angle_MAX_value   Angle_MAX_deviation```, for example ```1  2  120  240  15```, read the manual for more details.   
  - Run another script to preprate the final Uniconf input (molecule-uni.inp):
    - ```python3 /path/to/your/script/input_uniconf-CLUST.py molecule.CHR``` (e.g. for clusters)
    - ```python3 /path/to/your/script/input_uniconf-TM.py molecule.CHR``` (e.g. for transition metals)
    - ```python3 /path/to/your/script/input_uniconf-ORG.py molecule.CHR``` (e.g. for large organic molecules)
    - Adjust the lines in the scripts (```input_uniconf-CLUST.py, input_uniconf-TM.py, input_uniconf-ORG.py```) to meet your needs.

> [!NOTE]
> For any inquires, questions, suggestions, etc. do not hesitate to contact us: Yury.Minenkov"at"gmail.com (replace "at" with @)

> **When using this code please cite the following publications:**
> 1) "Uniconf: An Alternative Conformer Generator with Broad Applicability", Y. Minenkov, 2024, submitted [**Generic reference**]
> 2) "16TMCONF543: An Automatically Generated Data Set of Conformational Energies of Transition Metal Complexes Relevant to Catalysis" A. A. Otlyotov, T. P. Rozov, A. D. Moshchenkov, and Y. Minenkov Organometallics 2024, 43, 2232 – 2242 (DOI: 10.1021/acs.organomet.4c00246) [**For isolated molecules**]
> 3) "An Influence of Electronic Structure Theory Method, Thermodynamic and Implicit Solvation Corrections on the Organic Carbonates Conformational and Binding Energies" A. S. Ryzhako, A. A. Tuma, A. A. Otlyotov, and Y. Minenkov J. Comput. Chem. 2024, 45, 3004 – 30016 (DOI: 10.1002/jcc.27471) [**For molecular clusters**]
> 4) "A Comprehensive Guide for Accurate Conformational Energies of Microsolvated Li+ Clusters with Organic Carbonates" A. A. Otlyotov, A. D. Moshchenkov, T. P. Rozov, A. A. Tuma, A. S. Ryzhako, and Y. Minenkov Phys. Chem. Chem. Phys. 2024, 26, 29121 – 29132 (DOI: 10.1039/D4CP03487B) [**For molecular clusters**]
