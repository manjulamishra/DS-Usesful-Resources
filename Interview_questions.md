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
1. What is the difference between descriptive statistics
  and inferential statistics?
2. How would you explain a 95% confidence interval
  to an executive with no statistics background?
3. What is a t-test?
4. What are some different types of distributions
  and what are their qualities?
5. What are null and alternative hypotheses?
  Give an example.
6. When is more data better? When is it worse?
7. How do you keep up with economic and
  business news? How about data science news?

### Week 8:
1. What is a logistic function? What is the range of values of a logistic function?
    - f(z) = 1/(1+e -z )
    - The values of a logistic function range from 0 to 1. The values of Z vary from -infinity to +infinity.
    
2. Why is logistic regression very popular?
    - Helpful in classfication problems
    - It can handle binary as well as multi-class classification problems
    - It output the probabilities of obervations falling in different classes
    - Great when dependent variable is a categorical variable

3. How to interpret the results of a logistic regression model?
    - 
4. Why can’t linear regression be used in place of logistic regression for binary classification?
5. What is survival analysis and when would you use it? How is it different from other regression techniques?
6. What is qunatile regression and When would you use it?
7. In what circumstances Ridge regression might be an ideal choice? 
  
### Week 9:
1. In Python, what is the difference between a list and a tuple?
   - List is typed as [1,2,3]
   - Tuple is typed as (1,2,3)
   - Lists have mutable nature i.e., list can be changed or modified after its creation according to needs whereas
     tuples have immutable nature i.e., tuple can’t be changed or modified after its creation.
   - Lists have variable length, tuples have fixed length.
2. What is logistic regression? Provide an example for when it might be used.
   - Logistic Regression is a Machine Learning classification algorithm that is used to predict the probability of
     a categorical dependent variable. 
   - In logistic regression, the dependent variable is a binary variable that contains data coded as 1 
     (yes, success, etc.) or 0 (no, failure, etc.).
   - An example of when to use would be bank loan applications and whether they were accepted or denied.
   - Other examples would be whenever the dependent variable or label is a yes/no.
3. During analysis, how do you treat missing values?
   - Very dependent on how filling or dropping these values/rows/columns would affect your model.
   - It's important to understand the data before modifying it.
   - Use of pandas.isna().sum(), pandas.describe(), pandas.info() to understand the data.
   - Use of pandas.fillna() to fill NaNs with a certain value.
   - Use of pandas.dropna() to drop any row with NaN in any column.
   - Use of pandas.drop(column=[]) to drop any columns with NaN.
4. What is multicollinearity and how you can overcome it?
   - Multicollinearity is a state of very high intercorrelations or inter-associations among the independent variables.
   - High levels of Collinearity in a dataset is bad because it increases standard errors and therefore makes estimates
     of our coefficients less precise.
   - We test for high levels of collinearity by calculating the dataset's Variance Inflation Factor or VIF.
   - Use the correlation matrix to check levels of correlation between independent variables.
   - As a rule of thumb any variable that has a VIF > 10 needs to be dealt with (probably dropped from your model). 
   - If you see a VIF greater than 10 it is likely that two x variables are highly correlated.
5. Can you explain why you changed career paths?
   - Desire to learn.
   - Desire to take on more responsibility.
   - Desire to gain a new skill or grow a current skill.
   - Talk about why Data Science was interesting to you.
   - Talk specifically about the job for which you are currently interviewing.
   - Show excitement about the opportunity to learn some new skills and adapt to change.
   - Make sure you take time to describe your accomplishments, and all of the good that you’ve done for
     your current employer.
   - DON'T talk negatively about your previous job(s). Look ahead.
6. What are your salary requirements?
   - Do some research to understand the market salary range for the position, size of the company you’re
     interviewing with, location, and your experience level.
   - You will also want to think a bit about best case scenarios (what salary offer would make you say yes
     on the spot) and worst case scenarios (what salary offer would you walk away from).
  
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
