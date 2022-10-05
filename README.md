# ML4641

## Introduction
Image classification has a wide range of researched techniques and approaches which have been applied to a variety of problems. Our project is interested in exploring the application of this technology to classifying Pokémon. Existing techniques for classifying animals do exist, and it would be interesting to apply this technology to Pokémon types, which can be considered a loose analog for animal taxonomical groups (family, phylum, etc.). 

## Problem Definition
The classification of Pokémon by types can be considered to be an interesting toy problem of the real life problem of animal image classification. Advantages of working with Pokemon are that they are easily observable and replicable, and with the introduction of more recent entries into the Pokémon game franchise, it is feasible to build more robust Pokemon images not just from their official art, but from 3d models as well. Working on this classification problem will possibly offer insight into how Pokémon designers generate new ideas (what features, colors, etc. do they seem to associate with different types as designers?). 

## Methods
We will preprocess the [data](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types) by initially removing the gaps in the dataset. Then we will reduce and standardize the size of  each of the images so that our model doesn’t have to account for image size when processing. Lastly, we will augment the dataset by applying transformations on the images, such as inversion, and using unsupervised Principal Component Analysis (PCA), we implement feature reduction.
After the data is cleaned and preprocessed, we plan to use a supervised K nearest neighbors classification algorithm to classify the Pokemon into different types. The K neighbors classifier can be trained using part of the dataset and tested using the remaining part. We are using this algorithm because it performed well when dealing with a similar problem of snake species classification. This algorithm is also easy to understand, and functions as a good starting point for other algorithms.

## Potential results and Discussion
In order to measure the model performance we will use the accuracy, categorical cross entropy, multi-class F1, and confusion matrix as some of our metrics for classification. The model should be able to classify the Pokemon images into groups, through their given primary archetypes, with significant precision. The accuracy metric is a quintessential feature defining how accurate the model is. Categorical cross entropy will measure how distinguishable the probability distributions for each Pokemon type are from each other. Accuracy could be potentially misleading on imbalanced datasets, and therefore confusion matrix, owing to its versatility, would be another excellent tool for evaluating performance.
Since some types of Pokemon are significantly more common than others, it is expected that the confusion matrix will show a higher number of pokemon classified as the more common types (i.e. fire,water, etc.) than the actual amount of that type and vice versa. The multi-class F1 is expected to correspond with the categorical cross entropy as the more distinguishable the probability distributions are the better the precision and recall will be.

## References

1. Tabak, M. A., Norouzzadeh, M. S., Wolfson, D. W., Sweeney, S. J., VerCauteren, K. C., Snow, N. P., Halseth, J. M., Di Salvo, P. A., Lewis, J. S., White, M. D., Teton, B., Beasley, J. C., Schlichting, P. E., Boughton, R. K., Wight, B., Newkirk, E. S., Ivan, J. S., Odell, E. A., Brook, R. K., … Miller, R. S. (2018). Machine learning to classify animal species in camera trap images: Applications in ecology. Methods in Ecology and Evolution, 10(4). https://doi.org/10.1101/346809 
2. Han, Y., Zou, Z., Li, N., &amp; Chen, Y. (2022). Identifying outliers in astronomical images with unsupervised machine learning. Research in Astronomy and Astrophysics, 22(8), 085006. https://doi.org/10.1088/1674-4527/ac7386 
3. Amir, A., Zahri, N.A.H., Yaakob, N., Ahmad, R.B. (2017). Image Classification for Snake Species Using Machine Learning Techniques. In: Phon-Amnuaisuk, S., Au, TW., Omar, S. (eds) Computational Intelligence in Information Systems. CIIS 2016. Advances in Intelligent Systems and Computing, vol 532. Springer, Cham. https://doi.org/10.1007/978-3-319-48517-1_5
4. 

## Timeline
[Access Gantt Chart here](https://docs.google.com/spreadsheets/d/1C_5R84fuOJFV-A0jJgSX9z4PrilBJ4jo/edit?usp=sharing&ouid=107739152912878040423&rtpof=true&sd=true)

<img width="1292" alt="Screen Shot 2022-10-05 at 5 24 06 PM" src="https://user-images.githubusercontent.com/29692528/194166644-39d691f2-c7d2-45de-95f7-49648283de14.png">


## Contribution Table

| Aayush Mittal   | Eric Chen        | Janie Edgar      | Sera Biju        | Marin Hyatt      |
| ----------------|------------------| -----------------|------------------| -----------------|
|Potential Results| Introduction/Problem Def.| Potential Results| Methods          | Methods          |
| Discussion      | Contributions    | Discussion       | Datasets         | Datasets         |
