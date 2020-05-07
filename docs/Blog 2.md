##Reflection on our project journey 

This blog is written to document our reflection on what we have observed and learnt so far. We will share some difficulties we encounter and our takeaways from them. 
As we have discussed in our first presentation, the first step of our project is data collection. We located 3 different sources for getting our textual data, namely Reddit, Twitter and Stocktwits and Yahoo Finance for obtaining all earnings release. 
For getting earning scores from Yahoo, there is a Yahoo Earnings Calendar Scraper available on Github, we modified the code and successfully extract the desired data. It went super smooth. 
Let's talk about Reddit! There are several concerns with reddit data – firstly, there isn’t enough data! Seemingly, investors of the world don’t prefer Reddit as much as we believed them to. This leads to the lack of data in general for each company and earnings release pair. Secondly, unlike most other subreddits, r/investing does not have a very standardized set of acronyms and writing styles. This means that different users write about things in different ways, making text analytics slightly tougher. Third, following on from the previous issue, there is no one way to mention a specific company/stock. Some users will write the full name of the company, some will use the ticker and some will use an alternative short name. This makes the search functionality less effective than desired. Finally, reddit submissions come with upvotes, downvotes and comments. This means that the actual impact and correctness of a submission can be well judged by the amount of (good) attention that it gets. However, going back to the first issue, there aren’t enough people commenting or voting on posts which leaves us with all posts weighted equally. The key idea here is that selection of sources is very important for any sort of analysis. While Reddit can be a great source of textual data for many other purposes, it is probably not the best one for financial opinions. The biggest issue with reddit is just the lack of audience and users. However, Reddit does provide a lot of potential for text analysis given its very user-friendly API and a massive amount of data. 
Then for Stocktwits, it probably has the best textual data for financial analysis, in terms of, quantity, quality and relevancy. However, obtaining the data is a really painful process. The first and biggest roadblock is that Stocktwits doesn't allow web scraping and its API has a rate limit that only provides minimum amount of data, which can not be used for NLP and text analytics. Although we are a bunch of business students with limited tech background, this technical difficulty didn't scare us away as we have a philosophy that every problem can be solve by a line of code, if not, then go to Github. 
As our philosophy predicts, there is a solution on GitHub. We modified the established code for our project and we manage to get over the API rate limit, without knowing what exactly the code does and the complex programming knowledge behind. This doesn't mean programming knowledge is not important, but rather, this resonates with our course focus - application, or being able to use existing building blocks to design a something. For Twitter, we encountered the same thing and used the same solution. Our own coding skills were actually improved through reading and analyzing other people's established code. 
For data processing, things became a little bit easier. Our main challenge here is how to deal with the discrepancy between theory and practical applications. Even though we are provided with complete examples in lecture notes but in reality when we are doing text preprocessing we do have to decide whether a particular type of text poses meaning to our analysis. For example, we decided to remove the links and the symbols of the tickers in addition to the conventional methods looking at their high frequency of occurrences in our textual data. It is about how to make good use of what we learn from the lectures in a constructive way. 
Now all data is ready for running the model, we will follow along the lecture notes and let's see what will turn out. 