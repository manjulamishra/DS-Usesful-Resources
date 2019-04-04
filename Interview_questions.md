### Week 1.1: 

1. What data would you love to acquire if there were no limitations?
2. What would you do with that data (projects, startups, apps)?
3. Bring something for “Show and Tell” (screenshare) that got you interested in this data or shows why it is interesting to you.

### Week 1.2:

1. Why are you at Lambda School?
2. What did you do before Lambda School?
3. What is something interesting about you?

### Week 2:

1. What is the difference between quantitative and qualitative data? What are a few examples of each?
2. What are numpy and pandas and what are they used for?
3. How might you plot time-series data in a clear way? What would be a bad way to visualize it and why?
4. What is data science to you?
5. What is the most confusing topic from week one of class?

### Week 3:
Biases in data visualization

There are numerous types/forms of biases, such as technical, language bias, biased data narrative, replication bias. Good article here: https://alshams.github.io/responsibledata/bias-in-data-viz/
Can you find an example where the chart or other data visualization is misrepresenting the actual research? 
1. How might a visualization appear different to viewers from different cultures?
2. What are apophenia and confirmation bias and how do they affect the creation of visualizations?
3. At what point could a misleading chart become unethical?

### Week 4:
1. What is the difference between descriptive statistics and inferential statistics?
  * Descriptive statistics uses the data to provide descriptions of the population. 
  * Inferential statistics makes inferences and predictions about a population based on a sample of data.
2. How would you explain a 95% confidence interval to an executive with no statistics background?
  *  If we take 100 different samples and compute a 95% confidence interval for each, then approximately 95 of the 100 confidence intervals will contain the true mean value (μ)
3. What is a t-test?
  * t-test is a type of inferential statistic.
  * Used to determine if there is a significant difference between the means of two groups.
4. What are some different types of distributions and what are their qualities?
  * *Bernoulli Distribution* has only two possible outcomes, namely 1 (success) and 0 (failure), and a single trial. 
  * *Uniform Distribution* - Roll a fair die, the outcomes are 1 to 6. 
    * Probabilities are equally likely = the basis of a uniform distribution. 
    * All the n number of possible outcomes of a uniform distribution are equally likely.
  * *Binomial Distribution* - distribution where only two outcomes are possible.
    * Such as success or failure, gain or loss, win or lose.
    * AND the probability of success and failure is same for all the trials.
  * *Normal Distribution* represents the behavior of most of the situations in the universe.
    * The large sum of (small) random variables often turns out to be normally distributed.
    * Any distribution is known as Normal distribution if it has the following characteristics:
      * The mean, median and mode of the distribution coincide.
      * The curve of the distribution is bell-shaped and symmetrical about the line x=μ.
      * The total area under the curve is 1.
      * Exactly half of the values are to the left and right of the center.
  * *Poisson Distribution* is applicable in situations where events occur at random points of time and space.
    * Our interest lies only in the number of occurrences of the event.
    * A distribution is called Poisson distribution when the following assumptions are valid:
      * Successfull events must not influence outcomes of another event.
      * Probablity of success over short interval must be the same as P of success over long interval.
      * P of success in an interval approaches zero as the interval becomes smaller. 

5. What are null and alternative hypotheses? Give an example.
  * Null hypothesis sets the stage for an experiment by giving us something to compare to.
  * Question: "Does Sugar influence Hyperactivity?"
  * An example of a null hypothesis: "Hyperactivity is *unrelated* to eating sugar"
  * Another question: "How does cadmium in soil effect my plants?" 
  * Another example:  "Plant growth rate is *unaffected* by the presence of cadmium in the soil."
6. When is more data better? When is it worse?
  * More data is better when it contributes to the signal. 
  * More data is worse when it contributes to noise. 
7. How do you keep up with economic and business news? How about data science news?
  * I focus on economic and business news that is relevant. 
  * I am selective of who I follow on twitter and which blogs I follow.
  * Curating good sources means I am supplied with quality information continously on those platforms. 
  
### Week 8:
1. What is a logistic function? What is the range of values of a logistic function?
    ### f(z) = 1/(1+e -z )
    ### The values of a logistic function range from 0 to 1. The values of Z vary from -infinity to +infinity.
    
2. Why is logistic regression very popular?
    ### Helpful in classfication problems
    ### It can handle binary as well as multi-class classification problems
    ### It output the probabilities of obervations falling in different classes
    ### Great when dependent variable is a categorical variable

3. How to interpret the results of a logistic regression model?
    ### 
4. Why can’t linear regression be used in place of logistic regression for binary classification?
5. What is survival analysis and when would you use it? How is it different from other regression techniques?
6. What is qunatile regression and When would you use it?
7. In what circumstances Ridge regression might be an ideal choice? 

  
### week 11:
1. How are you today?
2. How is object-oriented programming different from functional programming? What are some advantages or disadvantages of each?
3. What is the relationship between modules, packages, dependencies, and namespaces in Python?
4.  What are some differences between Bayesian statistics and frequentist statistics? When might you use one over the other?
5.  How does a confusion matrix help you understand your model better?
6.  What is the alignment problem in artificial intelligence?
7.  We offer great flexibility in our employees’ scheduling? What would your ideal work week look like?

### Week 12:
1. So far in this sprint you've used SQLite, PostgreSQL, and MongoDB. For each of these, consider the following questions:

- What was easy about using this technology?
- What was hard about using this technology?
- What more would you like to learn about it?

Write a summary in the style of a possible blog post, and bring the
questions/discussion to class. Bonus - later on, follow up and complete a real
blog post about different database technologies!

### week 13:

1. What about our company excites you the most? (_assume it is a company in a field you are *NOT* excited about_)
2. What is pipelining and how might you build one in Python?
3. What is the inverse of the squish function?
4. You are on a boat and throw a suitcase overboard. Does the water level increase?
5. What would you do if a teammate changed your work without consulting you first?
6. Whats your current biggest DS-related weakness and what are your plans on it?
7. You don’t have a Phd. or a degree in a requisite field.  Why should we hire you?

### Week 14:

1. What was your biggest achievement in your last job?
2. Do you prefer working in a team or alone? Why?
3. What are two or three specific applications of data science that get you most excited?
4. What are some key differences between Python and Scala?
5. What is a method for determining if statistics published in an article are either wrong or presented to support the author’s point of view?
6. Explain what resampling methods are and why they are useful. What are their limitations?
7. In late 2016, a new recruit at Facebook designed a new feature to improve click-through rates on ads for political ads. They deployed their feature on a representative sample of users from across the country. The feature did not improve rates significantly in the general population, but it DID improve click-throughs for two groups: Female Texan college graduates between the ages of 30 and 35 and Male Floridian high-school graduates between 18 and 25.  The recruit’s manager was reviewing this data and had to decide whether to invest more time into testing/deploying it further.  What is the first question the manager should ask?
8. What would make you quit a job you just started?

### Week 16:

1. Good morning! What do you think of our new offices here?
2. What is the difference between a deep and a shallow copy?
3. What the heck are *args and **kwargs and when are they used?
4. How do data scientists work with backend engineers?
5. Give an example of a time you would use a decision tree?
6. How many golf balls would fit into a Boeing 747?
7. What was the most difficult task you’ve faced in your last job and how did you overcome it?
8. If your manager asked you to do some task with data that you believed was unethical, how would you respond?

### Week 17:
1. What do you want to do by joining this position?
2. What are the ML concepts covered at Lambda School?
3. What is a lambda function in Python?
4. What is ROC AUC?
5. What are sampling techniques and which ones have you used?
6. Why is Python interpreted?
7. What are the disadvantages of an interpreted language?
