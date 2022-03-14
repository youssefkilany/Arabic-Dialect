# Arabic Dialect

This repository hosts Django Application Deploying ML and DL Models for Arabic Dialects in texts Classification.

## Arabic Dialects
Arabic language many dialects across MENA, and among sources for people to communicate, twitter is a good source where we can get a huge amount of data to represent such diversity.
There's [a paper](https://arxiv.org/abs/2005.06557) discussed this already, and I encourage you to skim through it, you'll find it easy to follow with.

## Methods
I've used SGDClassifier, which performed quite well relatively to published results in [the paper](https://arxiv.org/abs/2005.06557).
Also, I've used a pretrained [AraBERT v0.2](https://huggingface.co/aubmindlab/bert-base-arabertv02) from HugginFace, which is helpful as they did most of the heavy lifting.

## TODOs:
- Nice & fancy UI
- Support TPU training for AraBERT Model
- Apply Out-of-core Classifitcation with proper setup
- 

## Resources:
[Arabic Dialect Identification in the Wild](https://arxiv.org/abs/2005.06557)
