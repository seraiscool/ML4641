# ML4641

## Introduction
Image classification has a wide range of researched techniques and approaches which have been applied to a variety of problems. Our project is interested in exploring the application of this technology to classifying Pokémon. Existing techniques for classifying animals do exist, and it would be interesting to apply this technology to Pokémon types, which can be considered a loose analog for animal taxonomic groups (family, phylum, etc.). 

## Problem Definition
The classification of Pokémon by types can be considered to be an interesting toy problem of the real life problem of animal image classification. Advantages of working with Pokemon are that they are easily observable and replicable, and with the introduction of more recent entries into the Pokémon game franchise, it is feasible to build more robust Pokemon images not just from their official art, but from 3d models as well. Working on this classification problem will possibly offer insight into how Pokémon designers generate new ideas (what features, colors, etc. do they seem to associate with different types as designers?). 

## Data Collection
The dataset used for classification was constructed out of two different datasets: a dataset listing Pokemon art and their names, and a dataset listing Pokemon sprite images and their names. The two datasets with images were augmented by flipping the images horizontally and rotating them 90 degrees, shown below:
  
![rotate1](https://user-images.githubusercontent.com/29692528/201534583-fc24f0db-ecd8-428f-bea8-f4d817632ad2.png)
![rotate2](https://user-images.githubusercontent.com/29692528/201534597-ab0941e0-6d15-455d-b86b-b2730cf27916.png)
![rotate3](https://user-images.githubusercontent.com/29692528/201534609-ee7a2708-bcbf-46f4-8751-cb80cf1da2e4.png)

The augmentation was done using the PIL library. The two augmented image datasets were then combined into one image dataset that contained both art and sprite images along with the Pokemon’s respective names. When the images were combined, they were also standardized to size 256 x 256, and the image backgrounds were all set to white. 
Since the sprite and art datasets used different naming conventions for their images, some data cleaning was necessary to standardize this for our models. Additionally, the art dataset did not include truth data at all, so we had to create a truth dataset by taking advantage of some information encoded in the naming convention of the images. 
	The next step in the data preprocessing stage was converting the images to feature vectors. Each image was either 125 x 125 or 256 x 256, so first the images were upscaled to 256 x 256 pixels using the cv2 library. Every image was now represented by a matrix with shape (256, 256, 3) – the 3 dimensions representing the r, g, and b values. The matrix was then flattened into a feature vector by taking the average pixel value across the rgb channels, leaving each image to be represented by a (65536, ) matrix. Finally, the image dataset was merged by Pokemon name with the dataset of Pokemon types, to result in a final dataset like this:


<img width="417" alt="Screen Shot 2022-11-13 at 12 13 26 PM" src="https://user-images.githubusercontent.com/29692528/201534680-e12cea4a-6ce2-4439-af5b-597332a74186.png">

A heat map was generated to visualize the number of each type of pokemon and collect data on how common each type in the dataset is. The density of each type will likely play a role in how well the types are classified. As such, the heat map was used to aid in model error and performance diagnosis.

![heat_map](https://user-images.githubusercontent.com/29692528/201534698-3597bb02-c3ac-4024-a149-d3c7139454b2.png)

Another 2-D heatmap represents how many Pokemon have each type as either its primary or secondary type. It is used to evaluate if there is a correlation between certain types--for example, we can see from the heatmap that the Normal type has a moderately strong correlation with the Flying type. It gave more information that many Pokemon in the dataset don’t actually have a secondary type, which is shown by the strong correlations with almost every type with the Other type (which represents not having a type).
![heat_map](https://user-images.githubusercontent.com/34498983/201546159-c3a5699a-2e00-428e-9d12-bd370dee8de5.png)

## Methods
Our team first ran PCA on the preprocessed data to prepare it for training. We tested different compression levels for PCA, using  image compression on samples from the datasets to visualize the image quality for varying numbers of components. It was observed that at one component only the colors clearly remain and at eighty components the image quality is very good. As such, we concluded that a component number around eighty would be well suited for PCA.
  
<img width="645" alt="Screen Shot 2022-11-13 at 12 15 05 PM" src="https://user-images.githubusercontent.com/29692528/201534759-1961c20e-e41f-45d5-b054-ac46e74da4ea.png">
<img width="554" alt="Screen Shot 2022-11-13 at 12 15 32 PM" src="https://user-images.githubusercontent.com/29692528/201534783-fd3d419a-c637-46e2-9c49-756e58c81f3c.png">

Considering how even with image compression, the number of components necessary to retain a reasonable amount of variance was something around 80-150. Obviously, this is far and away impossible to visualize, so we considered TSNE as a means to visualize our data on a two dimensional graph. At a high level, TSNE categorizes pairs of data points based on probability distributions, grouping similar data points together while separating dissimilar ones. The main draw of TSNE is that unlike other dimension reduction methods (such as PCA) it is nonlinear. While not typically used for image classification based on our research, its ability to map high dimensional data to 2 or 3 dimensions was very appealing and at least seemed worth some exploration. Ultimately, running TSNE on the compressed versions of the datasets yielded these results:

<img width="327" alt="Screen Shot 2022-11-13 at 12 15 54 PM" src="https://user-images.githubusercontent.com/29692528/201534805-69b226a3-e760-4c07-ac83-0b871ef70566.png">

<img width="316" alt="Screen Shot 2022-11-13 at 12 16 17 PM" src="https://user-images.githubusercontent.com/29692528/201534826-20c521f0-0364-4a69-af77-1bb69abf0856.png">

Obviously, there are no clear trends between types that are observable from these outputs. This isn’t particularly surprising; Pokémon can vary strongly within the same type, and considering how well PCA performed, it would have been suspicious if TSNE drastically outperformed it. It is worth noting the small abnormal “cluster” present in the sprite set; the grouping doesn’t appear to have any meaningful intracluster patterns, so it’s likely this separation from the main mass of data is due to some other unobserved reason. If we were to continue exploring this space, we would likely consider looking at the individual data points in a small region of each of these graphs to see how TSNE was sorting images as well as increasing the number of components as a potential feature reduction approach. 

Our team first used KNN as a supervised machine learning method, with the implementation coming from the sklearn library. The data was first split into training and testing sets, with 25% of the data set aside for testing. Since some (but not all) Pokemon have primary and secondary types, just the primary type was used for KNN. After the types were encoded, KNN was fit to the dataset, with the number of neighbors being 7. The results of running KNN are discussed later, but it’s worth noting that since KNN algorithm is fairly simple, we were not necessarily expecting amazing results.

After we ran KNN, we implemented a Convolutional Neural Network using the keras library and used that to predict Pokemon types. The CNN had 3 convolutional and max pooling layers, followed by a dense layer, a dropout layer, and another dense layer. The data was randomly split into  2326 training samples and 581 testing samples. After that, the CNN was trained for 40 epochs with a batch size of 32. 
	We used a CNN because it makes the most sense when dealing with images. It’s also a more complex approach than a KNN, so it has a higher chance of successfully classifying Pokemon types.



## Results and Discussion
To evaluate the KNN model, we used sklearn’s classification report to get some basic statistics for each class. As is shown in the image below, most of the scores were very bad for each class. Some reasons behind this could be the lack of data points for many labels – for example, only one Pokemon in the testing set was a Flying type. This hypothesis is also supported by higher scores for Pokemon with more common types. For example, the Grass type (one of the more common types) had one of the highest precision, recall, and F1 scores.

<img width="430" alt="Screen Shot 2022-11-13 at 12 17 06 PM" src="https://user-images.githubusercontent.com/29692528/201534868-36329faa-1395-4e6b-8d56-3d6f0fa136d6.png">

From our low precision and recall values, one can gather that our model is currently producing a large number of false positives and false negatives. This becomes particularly pronounced when Pokemon class metrics are skewed. One potential reason could be that the synonymous color palette for closely-related pokemon types (such as Ice and Water) is causing the KNN based model to leverage the results in the favor of the more prevalent archetype.
Another thing that we can glean from the report is that the classes with relatively distinct color palettes such as Fairy, Psychic etc. fared better than their counterparts. The more range features or colors within the distinct types, the more generally easier it is for the model to classify them. 

Below is the confusion matrix for the KNN  results:

<img width="453" alt="Screen Shot 2022-11-13 at 12 17 48 PM" src="https://user-images.githubusercontent.com/29692528/201534903-8e7d993e-7baf-414a-86ca-a0e1f43c427f.png">

In which each element of the confusion matrix Ci,j represents the number of known pokemon in a specific type i  and the number predicted to have a type j. From left to right for the columns and top to bottom for the rows, the types are Bug, Dark, Dragon, Electric, Fairy, Fighting, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel,  and Water. Reading the diagonal of the matrix gives the number of correctly predicted pokemon for each corresponding above type. 

For example, 11 bug-type pokemon were mistakenly predicted to be of type ground, but 6 bug-type pokemon were predicted correctly. The 0.11 precision value, 0.24  recall value,  and 0.15 F1 score for grass type pokemon is further supported by the proper classification of 9  grass type pokemon and the occurrence of high numbers of other type pokemon being classified as ground (10 Normal, 12 water). While the proper classification of 9 pokemon for a given type is not ideal, it is the highest number of pokemon predicted correctly for a given type causing these model metrics to be some of the highest. The grass type misclassification for Bug and Normal types supports the theory that the low model accuracy is most likely related to overlapping in their typical color palettes in addition to the occurrence of pokemon that do not visually look like their type commonly does. 

The second highest amount of properly classified pokemon (8) was for the Normal type. This combined with the normal type containing the most pokemon and the most predicted pokemon, caused this type to have the highest precision value along with a high F1 score and a moderate recall value. The misclassification of other types as a normal type, 10 ground, 10 flying, and 9 bug once again could be supported by similar color palettes used by these types. However, another factor driving this is that there are a large number of pokemon whose primary types are ground or flying and whose secondary types are normal. These Pokemon would have varying levels of similarity to those classified as a primary type of normal which could explain their misclassification. 

It is noted that 9 out of the 18 Pokemon types had zero correct model classifications. These correspond to the types that have values of 0 for precision, recall, and F1 score as to be expected. 

The large number of types with no correctly classified pokemon and the relatively low percentages of correctly classified pokemon reflect the relatively low accuracy of the model. 

The categorical cross-entropy loss is 19.681730524113725 and measures how distinguishable the probability distributions for each Pokemon type are from each other. Based on the total number of types (18), it can be concluded that there is currently a large amount of error between the predicted type and the actual type as the normalized cross-entropy loss would be slightly bigger than 1. The difference in probability distributions is likely caused by some types having similar color palettes, low occurrences of certain types, and pokemon exhibiting characteristics of their secondary types which can confuse the model. 

We used sklearn’s classification report to evaluate the CNN model and get training and validation accuracy statistics at each epoch. Most of the scores for the training accuracies plateau  at around 96%, while the validation accuracies cap at 72%. Some explanations behind this can be how the training data lack points for many labels due to how the CNN split the training and testing data. It decreases the potential validation accuracy for the remaining labels due to false positives and negatives from the missing ones in the training data. 

Below is the CNN results for some of the  epochs:

<img width="517" alt="Screen Shot 2022-12-06 at 6 27 48 PM" src="https://user-images.githubusercontent.com/29692528/206047341-3282b4f2-bee5-4acb-b997-a0e71bca0560.png">

To elaborate further, we note that sparse categorical  and top k sparse categorical accuracy  for the training data is within the same range of values. However, there is a difference within the ranges for the top k sparse categorical accuracy  and the validation accuracy for the testing data.  Some reasons behind it can be that the more common types of Pokemon are more prevalent in both training and testing data, thus the model is able to predict Pokemon with the same types more accurately. If you take the top K categorical accuracies for the common types of Pokemon, it improves the top k sparse categorical accuracy  in comparison to the total validation  accuracy. 	
Based on the figures below, the graph plateaus at around 20-30 epochs even though we run the model for around 100 epochs. The model readjusts its weights accurately to reflect the training data. CNN is more useful in image recognition since the model emphasizes the distinctive features of each image it classifies by computing its weights again for those features.

<img width="582" alt="Screen Shot 2022-12-06 at 6 28 18 PM" src="https://user-images.githubusercontent.com/29692528/206047427-40813370-b45e-4348-9508-6028afcd514a.png">

CNN performs much better than KNN, probably due to the more sophisticated nature of the model. Some of very common miscalculations are similar color palettes between some types, rare Pokemon primary and secondary types, and secondary type characteristics skew analysis when the model focuses on primary type only.

## References

1. Tabak, M. A., Norouzzadeh, M. S., Wolfson, D. W., Sweeney, S. J., VerCauteren, K. C., Snow, N. P., Halseth, J. M., Di Salvo, P. A., Lewis, J. S., White, M. D., Teton, B., Beasley, J. C., Schlichting, P. E., Boughton, R. K., Wight, B., Newkirk, E. S., Ivan, J. S., Odell, E. A., Brook, R. K., … Miller, R. S. (2018). Machine learning to classify animal species in camera trap images: Applications in ecology. Methods in Ecology and Evolution, 10(4). https://doi.org/10.1101/346809 
2. Han, Y., Zou, Z., Li, N., &amp; Chen, Y. (2022). Identifying outliers in astronomical images with unsupervised machine learning. Research in Astronomy and Astrophysics, 22(8), 085006. https://doi.org/10.1088/1674-4527/ac7386 
3. Amir, A., Zahri, N.A.H., Yaakob, N., Ahmad, R.B. (2017). Image Classification for Snake Species Using Machine Learning Techniques. In: Phon-Amnuaisuk, S., Au, TW., Omar, S. (eds) Computational Intelligence in Information Systems. CIIS 2016. Advances in Intelligent Systems and Computing, vol 532. Springer, Cham. https://doi.org/10.1007/978-3-319-48517-1_5

## Timeline
[Access Gantt Chart here](https://docs.google.com/spreadsheets/d/1C_5R84fuOJFV-A0jJgSX9z4PrilBJ4jo/edit?usp=sharing&ouid=107739152912878040423&rtpof=true&sd=true)

<img width="1292" alt="Screen Shot 2022-10-05 at 5 24 06 PM" src="https://user-images.githubusercontent.com/29692528/194166644-39d691f2-c7d2-45de-95f7-49648283de14.png">


## Contribution Table

<img width="574" alt="Screen Shot 2022-12-06 at 6 28 57 PM" src="https://user-images.githubusercontent.com/29692528/206047506-29d4b6c1-f33a-4d7e-9293-462dd44a0bd8.png">


| Aayush Mittal   | Eric Chen        | Janie Edgar      | Sera Biju        | Marin Hyatt      |
| ----------------|------------------| -----------------|------------------| -----------------|
|Dimensionality reduction - PCA implementation| TSNE implementation/visualization | Data visualization (heat map, image generation) | Data visualization (2nd heatmap -2d matrix)| Dataset augmentation         |
| Results     | Dataset Cleaning (file/ label formats)   | Results     | Results        | Data cleaning         |
|Discussion | | Discussion | Discussion| Feature vector generation|
| | | | | KNN implementation |


