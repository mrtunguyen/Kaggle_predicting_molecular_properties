This folder contains materials to reproduce the submissions files that contributed to the final solution which finished in 5th place of the kaggle competition [Predicting Molecular Properties](https://www.kaggle.com/c/champs-scalar-coupling)

See the complete details of our solution [here](https://www.kaggle.com/c/champs-scalar-coupling/discussion/106864)

### Idea 
The architecture is based on the paper [Graph Networks as a Universal Machine Learning Framework for Molecules and Crystals](https://arxiv.org/abs/1812.05055) with some changes to adapt to the use cases.

### Requirement

1. Hardware 
- CPU: 12 cores
- Memory: 32 GB
- GPU: 1 GTX 2080 Ti

2. Software:
- CUDA 10.0 CuDNN 7.4
- Anaconda Python 3.7 2019.03
- pytorch==1.1.0
- pytorch_geometric
- openbabel, rdkit

### How to train? 

- Generate data graph for every molecule:   
python data/data.py --data_dir=kaggle/data/csv --split_dir=kaggle/data/split --graph_dir=kaggle/data/graph

- Training: 
    - first model: python train.py --out_dir=kaggle/output --model=model1 --optim=adam
    - second model: python train.py --out_dir=kaggle/output --model=model2 --optim=adam
    - third model: python train.py --out_dir=kaggle/output --model=model1 --optim=ranger

### How to make prediction?
- python submit.py --out_dir=kaggle/output/submit --model=model1 --checkpoint=kaggle/output/checkpoints/checkpoint_01.pth


#### Credit
Credit to [Cher Keng Heng](https://www.kaggle.com/hengck23) for his starter kit code. 