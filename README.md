# ClusteringOfWords
Clustering of words, csv format file ,using K-Means algorithm

Clustering of tweets
By Qëndresa Bekaj, Ardita Berisha students of University of Prishtina "Hasan Prishtina"
Computer Science field, 19 June 2019 


In this project we used a dataset which contains around 200000 tweets as a csv file. We chose K-means as a algorithm for clustering.
At the beginning of our code we preprocessed tweets by removing url, http ,ftp ,short words ,stop words ,punctuation marks ,hashtags ,words with longer ocurring letters than two,mentions, numbers ,@-signs ,etc. 
Our next step was using elbow to find the most suitable number of clusters that we will use as a parameter to the K-means algorithm.
Firstly we checked elbow with a range of 1 to 10 clusters. But after checking the graph it seemed like the suitable value for the number of clusters was bigger so we continued by trying the range 1 - 15 then 1-25. The last one resulted to 10 clusters but for a more preferable result you can check a different range like 1-50.
We gave this number as a parameter to K-means so it gave us the result of 10 clusters. We tested different parameters in K-means and decided to analyze the results (2 of them given below).

<p>
<br> Cluster 0:  just  new  people  breaking  like  obama  don  black  hillary  white
<br>Cluster 1:  cnn  jaketapper  cnnpolitics  brianstelter  ananavarro  andersoncooper  cnnsitroom  cnni  theleadcnn  ac
<br>Cluster 2:  trump  president  donald  breaking  anti  just  supporters  video  obama  look
<br>Cluster 3:  police  wounded  shootings  shooting  officer  chicago  killed  suspect  dead  shot
<br>Cluster 4:  county  tax  gun  control  san  reform  diego  cook  cuts  sheriff
<br>Cluster 5:  children  play  games  hashtag  game  don  pay  black  parents  mother
<br>Cluster 6:  man  shot  police  killed  charged  shooting  old  year  woman  death
<br>Cluster 7:  rt  realdonaldtrump  day  chicago  year  time  video  make  woman  san
<br>Cluster 8:  says  nfl  trump  anthem  players  player  breaking  kaepernick  stand  protesters
<br>Cluster 9:  world  series  cubs  war  just  cup  trump  people  like  women
</p>

<br>Cluster 0:  just  new  breaking  like  cnn  hillary  don  hedgebz  year  old
<br>Cluster 1:  people  rt  police  black  realdonaldtrump  day  time  video  white  woman
<br>Cluster 2:  chicago  school  high  police  area  shot  shootings  shooting  wounded  students
<br>Cluster 3:  america  great  make  dare  click  patriots  save  join  trump  fight
<br>Cluster 4:  says  trump  latest  obama  hillary  president  police  clinton  white  new
<br>Cluster 5:  make  know  don  people  need  things  let  want  like  sure
<br>Cluster 6:  killed  wounded  crash  shootings  man  shooting  police  woman  south  shot
<br>Cluster 7:  man  shot  police  charged  shooting  old  death  year  arrested  fatally
<br>Cluster 8:  trump  president  donald  breaking  anti  just  supporters  video  look  clinton
<br>Cluster 9:  obama  trump  president  michelle  barack  admin  just  breaking  administration  clinton


The clusters seemed to contain their own story mostly revolving to political issues and tragedies. Some of the tweets seemed to talk about shootings stories which happened in Chicago. 
Some of them were talking about the death of an officer during the shootings which happened in Chicago. 
There were also some other tweets talking about Chikago and at the same time some high school students which were probably wounded as a result of shootings which might have happened aroud the school area.
In the political side, the tweets were mostly revolving to different political figures like Obama, Trump, Clinton as you can see in the clusters above or relate to North Korea, Iran and other political issues.

At the end of the code we took into consideration checking if tweets were being clustered correctly. 

<br>print("in which cluster does this post takes part:")
<br>Y = vectorizier.transform(["Im voting for Donald Trump"])
<br>prediction = model.predict(Y)
<br>print("In cluster number" + str(prediction))

This part of the code predicted in which cluster the post given would take part. In the second example of the clusterings above it resulted to the 8 cluster which seemed as a good choice because among all the clusters this one seem to be more related to our post.

