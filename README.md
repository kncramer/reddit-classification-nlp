# Project 3
---
## Fantasy Vs. Science Fiction
 
Fantasy and Science Fiction are often mentioned in the same breath, so I want to ask: how much interest is there in the crossover of the Fantasy and Science Fiction genres for an aspiring writer to pursue? I'm seeking to find how separate they actually are. 

By seeing how well I can train a model to differentiate between posts taken from the [fantasy](https://www.reddit.com/r/Fantasy/) and [scifi](https://www.reddit.com/r/scifi/) subreddits on [Reddit.com](https://www.reddit.com/), I should get an idea of how much overlap is currently between the two genres. 

|Feature|Type|Discription|
|---|---|---|
|**title**|*string*|Title of the subreddit post|
|**post**|*string*|Text content of the subreddit post|


---
## Analysis

There were several words that I found strongly correlated to each subreddit. Not surprisingly, the word fantasy is often mentioned in fantasy subreddits and some iteration of sci-fi is often mention in scifi subreddits. I also found the vast majority of book/reading mentions occurred in fantasy subreddit posts and the majority of movie mentions occurred in scifi subreddit posts.

As for crossover mentions, fantasy subreddit posts were more open to discussing scifi topics.

|Genre|Total mentions|Scifi proportion|Fantasy proportion|
|---|---|---|---|
|**fantasy**|2,085|3.79%|96.21%|
|**scifi**|585|82.74%|17.26%|

Below are the overall top ten words and their percentage of appearance that were mentioned in either post text or their titles:

|Word|Fantasy|Scifi|
|---|---|---|
|**book**|3184 / 85%|581 / 15%|
|**wa**|1505 / 68%|717 / 32%|
|**fantasy**|2006 / 96%|79 / 4%|
|**like**|1404 / 73%|519 / 27%|
|**character**|1282 / 87%|189 / 13%|
|**read**|1202 / 84%|235 / 16%|
|**series**|1111 / 81%|269 / 19%|
|**just**|968 / 71%|397 / 29%|
|**story**|982 / 73%|363 / 27%|
|**http**| 839 / 76%|266 / 24%|



I focused mainly on accuracy and F1 score when building my production model because I wasn't worried about one genre of subreddit being misclassified more than the other. I ended up using all of the text from titles and posts, and processed all text by shortening to root lemmas and further processing with CountVectorizer. My final model was a StackingClassifier that utilized my top performing tuning models (LogisticRegression, AdaBoostClassifier, and RandomForestClassifier) and LogisticRegression as the level two model. The final accuracy was 92.04% and the final F1 score was 92.57%. The stacked model also performed very well with the ROC Curve, having an area under the curve of 0.98.


---
## Conclusion and Insights

With how well the final model performed in accurately guessing for both subreddits, I can say with the misclassification rate of about 8% there is not a strong interest or desire for crossover stories including fantasy and science fiction. I would also recommend with how much more often books and reading were mentioned in the fantasy subreddit posts, a writer should have more success with a fantasy novel. However, if they are more interested in science fiction then it would be worth considering writing a screenplay since movies were mentioned more frequently in the scifi subreddits.


