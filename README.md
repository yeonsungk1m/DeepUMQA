# DeepUMQA
Ultrafast Shape Recognition-based Protein Model Quality Assessment using Deep Learning

Developer:
Saisai Guo
College of Information Engineering
Zhejiang University of Technology, Hangzhou 310023, China
Email: 2111903076@zjut.edu.cn

Contact:
Guijun Zhang, Prof
College of Information Engineering
Zhejiang University of Technology, Hangzhou 310023, China
Email: zgj@zjut.edu.cn

1. INSTALLATION
- Python > 3.5
- PyTorch 1.3
- PyRosetta
- Tested on Ubuntu 20.04 LTS

2. RUNNING
```
usage: DeepUMQA.py [-h] [--modelpath MODELPATH] [--pdb] [--csv] [--leaveTempFile] [--process PROCESS] [--featurize]
                     [--reprocess] [--verbose] [--ensemble]
                     input ...

arguments:
  input                 path to input
  output                path to output (folder path, npz, or csv)

optional arguments:
  -h, --help            show this help message and exit
  --pdb, -pdb           Running on a single pdb 
  --csv, -csv           Writing results to a csv file 
  --per_res_only, -pr   Writing per-residue accuracy only 
  --leaveTempFile, -lt  Leaving temporary files 
  --process PROCESS, -p PROCESS
                       
  --featurize, -f       Running only the featurization part 
  --reprocess, -r       Reprocessing all feature files 
  --verbose, -v         Activating verbose flag 
  --ensemble, -e        Running with ensembling of 4 models. 
                   
```

# Running on a folder of pdbs

python DeepUMQA.py -r -v input output

# Feature extraction

python DeepUMQA.py --featurize input/ outputFea/

# Traning

python train.py  models/


3. DISCLAIMER
The executable software and the source code of DeepUMQA is distributed free of charge as it is to any non-commercial users. The authors hold no liabilities to the performance of the program.
