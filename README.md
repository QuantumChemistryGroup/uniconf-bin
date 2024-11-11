# Uniconf
This repository **Uniconf** contains:
1) The Uniconf computer program for conformational search/sampling in isolated molecules and molecular clusters
2) A few Python 3 scripts to prepare input files / analyse the Uniconf results (if needed)

## Prerequisites
1) Linux operational system (for Uniconf)
2) Python 3 (for scripts)

## Running the code
### Preparation of input files
There are two ways to generate the Uniconf programs input files:
1. Manual preparation with your editor of choice. Please, see folder ```INPXYZ.zip``` for examples. In the examples, feel free to modify MK, ITER1 & ITER2 values for quick testing of the Uniconf.
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
### Test case: planar conformers of glycine
```/path/to/program/uniconf m1_00_GLY-uni.inp```
where m1_00_GLY-uni.inp is 
```$BOND
1 5 180 180 0
5 7 180 180 0
1 3 180 180 0 
$END
$ALGO
ALGO=CONF CONNECT=WRITE library=nlopt optloc=nlopt_ln_sbplx 
MAXDISTDIff=0.1 EDIFF=0.1 DIST=1.35 RMSD=0.1 MAXCLUST=100000 population=0
HB1=6.71 HB2=3.55 HB3=0.75 HCHRG=0.25 OCHRG=-0.5 KEL=1.0 KVW=1.0 KGD=0 TESTSIZE=1e-3
STRATEGY=1 SCALE=0.84 CLUSTERPROPERTY1=IXX SORT=d2
MK=0 ITER1=300 KMEANS=-1  MAXCONF=100000000 COM=0
ITER2=33000 KMEANS1=-1 MAXCONFPRINT=55000 
$END
$MOLECULE
  C  0.489539550 -0.137286825  0.000000000
  O  0.415700001 -1.343866228  0.000000000
  O  1.668983011  0.530543901  0.000000000
  H  2.366598269 -0.144335929  0.000000000
  C -0.689952803  0.817171210  0.000000000
  H -0.587142605  1.473033075  0.866245499
  N -1.995924447  0.203004587  0.000000000
  H -2.079505439 -0.407088216  0.803719497
  H -2.079505439 -0.407088216 -0.803719497
  H -0.587142605  1.473033075 -0.866245499
$END
$CHARGE
    0.597023 
   -0.555619 
   -0.666597 
    0.471514 
    0.311935 
   0.0376145 
   -0.950567 
   0.3585405 
   0.3585405 
   0.0376145 
$END
```
> [!NOTE]
> Useful information that users should know, even when skimming content.

> **When using this code please cite the following publications:**
> 1) "Uniconf: An Alternative Conformer Generator with Broad Applicability", Y. Minenkov, 2024, submitted [**Generic reference**]
> 2) "16TMCONF543: An Automatically Generated Data Set of Conformational Energies of Transition Metal Complexes Relevant to Catalysis" A. A. Otlyotov, T. P. Rozov, A. D. Moshchenkov, and Y. Minenkov Organometallics 2024, 43, 2232 – 2242 (DOI: 10.1021/acs.organomet.4c00246) [**For isolated molecules**]
> 3) "An Influence of Electronic Structure Theory Method, Thermodynamic and Implicit Solvation Corrections on the Organic Carbonates Conformational and Binding Energies" A. S. Ryzhako, A. A. Tuma, A. A. Otlyotov, and Y. Minenkov J. Comput. Chem. 2024, 45, 3004 – 30016 (DOI: 10.1002/jcc.27471) [**For molecular clusters**]
> 4) "A Comprehensive Guide for Accurate Conformational Energies of Microsolvated Li+ Clusters with Organic Carbonates" A. A. Otlyotov, A. D. Moshchenkov, T. P. Rozov, A. A. Tuma, A. S. Ryzhako, and Y. Minenkov Phys. Chem. Chem. Phys. 2024, asap (DOI: 10.1039/D4CP03487B) [**For molecular clusters**]
