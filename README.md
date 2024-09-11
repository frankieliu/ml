# ml

# boosting vs bagging
https://blog.mlreview.com/gradient-boosting-from-scratch-1e317ae4587d


# converting 
## conda

conda init bash

copy from c:\Users...\.bash_profile to
~/bin/conda_stuff


conda info --envs
conda env list

conda remove -n <envname> --all -y
conda env remove -n <envname> -y

conda clean -a # remove tarballs

conda rename -p <path> newname

Install with multiple libraries
conda create -n <name> anaconda

## David Reed

### Success Hacks
1. Be prepared
2. Attend every class
3. Participate in class
4. Attempt all assignments
5. Advocate for yourself
6. Keep goal
7. Consistency is key


### Support features
1. Post class videos
2. Coaching sessions on Wed
3. Discord
4. TAs
5. Use academic support (SSAs)
6. Support tickets

# Multimodal training
Diffusion model 
- more graceful
- not for overfitting

Overfit
- generalize and specialized
- control depth and width
- Resnet, dropout
- Top down
- Residual connection
- Not introducing to penalize
  - whole network
- stop co-adaptation
  - Preventing one part doing the same as another task 

- Overfit and generalize every level

2d modality
one modality may not map with another modality

k-near neighbor

1. Shop talk
2. Noise is helping to regenerate them

# papers to read

https://blog.mlreview.com/gradient-boosting-from-scratch-1e317ae4587d
https://blog.mlreview.com/gradient-boosting-from-scratch-1e317ae4587d

https://github.com/hurshd0/must-read-papers-for-ml
https://github.com/aimerou/awesome-ai-papers
https://github.com/terryum/awesome-deep-learning-papers
https://github.com/elicit/machine-learning-list
https://github.com/thunlp/RCPapers
https://github.com/dair-ai/ML-Papers-of-the-Week
https://github.com/daturkel/learning-papers

https://docs.google.com/document/d/1nd4-CsavBD1hmvdyokc5OYiK7pThJttrCphuReJeO7k/edit?tab=t.0

The Kernel Trick in Support Vector Classification | by Drew Wilimitis | Towards Data Science
https://towardsdatascience.com/the-kernel-trick-c98cdbcaeb3f
Kernel 

SVM
Tabular data can get away with decision trees

SVM basically transform the data into kernels then you can do vector stuff on them like
SVM  - good for images and audio

But NN nowadays for this kind of data
---
