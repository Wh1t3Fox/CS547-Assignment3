# Purdue CS54701 - Spring 2015

##  CS54701 Assignment 3: Collaborative Recommendation Algorithm  

## Movie Recommendation System

In this assignment, you will develop different algorithms to make  recommendations for movies.

###The Training Data

The training data: a set of movie ratings by 200 users (userid:  1-200) on 1000 movies (movieid: 1-1000). The data is stored in a 200 row x 1000  column table. Each row represents one user. Each column represents one movie. A  rating is a value in the range of 1 to 5, where 1 is "least favored" and 5 is  "most favored". Please NOTE that a value of 0 means that the  user has not explicitly rated the movie.

Please download the training data here: [train.txt][2].

### The Test Data

There are three test files: [test5.txt][3], [test10.txt][4] and [test20.txt][5].

[test5.txt]  A pool of movie ratings by 100 users (userid: 201-300). Each user has already  rated 5 movies. The format of the data is as follows: the file contains 100  blocks of lines. Each block contains several triples : (U, M, R), which means  that user U gives R points to movie M. **Please note that  in the test file, if R=0, then you are expected to predict the best possible  rating which user U will give movie M.** The following is a block for  user 262. (line 5588-5595 of test5.txt)


262 259 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// user 262 gives movie 259 3 points.  
262 310 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // user 262 gives movie 310 5 points.  
262 321 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // user 262 gives movie 321 5 points.  
262 323 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // user 262 gives movie 323 2 point.  
262 358 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // user 262 gives movie 358 1 point.  
262 11 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// need to predict user 262's rating for movie 11  
262 22 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // need to predict user 262's rating for movie 22  
262 100 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ...


**ATTENTION**: Please make  the prediction block by block: every time when you are making predictions for  user U, please assume that you **ONLY** know the knowledge of the training  data (train.txt) and the existing 5 ratings for this user. In another words,  please DO NOT use the knowledge of any other blocks in the test file when making  predictions.

The format of test10.txt and test20.txt is nearly the same as test5.txt, the only difference is that: in test10.txt, 10 ratings are given  for a specific user; in test20.txt, 20 ratings are given for a specific user.

Please make sure your predicted ratings are from 1 to 5. Otherwise, the grading system will return error.

## Tasks

Your task is to design and develop collaborative filtering  algorithms that predict the unknown ratings in the test data by learning users'  preference from the training data.

Please complete the following experiments:

**1\. Implement the Memory-Based Collaborative  Filtering Algorithm (40 pts)**

Please implement two versions of the memory-based collaborative filtering  algorithm as the Pearson Coefficient method and the vector similarity method

For more detailed information you can refer to

Breese J. S., Heckerman D., Kadie C. (1998).  Empirical Analysis of Predictive Algorithms for Collaborative Filtering.  ([Pdf][7])

**2\. Implement your algorithm 1 (15 pts)**

**3\. Implement your algorithm 2 (15 pts)**

You can try different extensions of the memory-based algorithm (e.g.,  algorithms in the above paper).

You can also try different model-based methods. Some references can be found:

Hofmann, T., &amp; Puzicha, J. (1999).  Latent Class Models for Collaborative Filtering. _In the Proceedings of  International Joint Conference on Artificial Intelligence. ([pdf][8])_

Pennock, D. M., Horvitz, E.,  Lawrence, S., &amp; Giles, C. L. (2000). Collaborative Filtering by Personality  Diagnosis: A Hybrid Memory- and Model-Based Approach. In the Proceeding of the  Sixteenth Conference on Uncertainty in Artificial Intelligence. ([pdf][9])

Si, L. &amp; Jin. R. (2003). Flexible mixture model for collaborative filtering.&nbsp;  &nbsp;In the Proceeding of the International Conference  of Machine Learning. ([pdf][10])

**4\. Results Discussion (25 pts)**

**Please provide the following information**

1. The accuracy of the algorithms;&nbsp; Do you think  the values are reasonable? How can you justify the results by analyzing the  advantages and disadvantages of the algorithms

2. How long each algorithm takes to complete the prediction? Discuss the  efficiency of the algorithms.

**5\. Results Competition (5 pts)**

To make the homework a little more interesting; 5  points will be assigned according to the performance of your recommendation  system. The best performance of the three algorithms from each student will be  recorded and compared. 5 full points will be assigned to the top 3 players, 4  points for players of ranks 4-6, 3 points for ranks 7-9, 2 points for ranks 10-12, and lastly 1 point for ranks 13-15.

[1]: http://www.math.mtu.edu/~msgocken/intro/intro.html "http://www.math.mtu.edu/~msgocken/intro/intro.html"
[2]: train.txt "train.txt"
[3]: test5.txt "test5.txt"
[4]: test10.txt "test10.txt"
[5]: test20.txt "test20.txt"
[6]: submit.html
[7]: http://research.microsoft.com/en-us/um/people/heckerman/bhk98uai.pdf "http://research.microsoft.com/en-us/um/people/heckerman/bhk98uai.pdf"
[8]: http://www.cs.brown.edu/~th/papers/HofmannPuzicha-IJCAI99.pdf "http://www.cs.brown.edu/~th/papers/HofmannPuzicha-IJCAI99.pdf"
[9]: ftp://ftp.research.microsoft.com/pub/ejh/cfpd.pdf "ftp://ftp.research.microsoft.com/pub/ejh/cfpd.pdf"
[10]: http://www.cs.purdue.edu/homes/lsi/ICML_2003.pdf "http://www.cs.purdue.edu/homes/lsi/ICML_2003.pdf"
[11]: mailto:yanhan@purdue.edu
