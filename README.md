# Bankmarketting

Data Analysis and Model Building(Deposit prediction) - Bank Marketing Campaign

This is data-set that describe Portugal bank marketing campaigns results. Conducted campaigns were based mostly on direct phone calls, offering bank's clients to place a term deposit. If after all marking affords client had agreed to place deposit - target variable marked 'yes', otherwise 'no'.

feature

1 age|int64|age in years

2 job|object|type of job('management' 'technician' 'entrepreneur' 'blue-collar' 'unknown','retired' 'admin.' 'services' 'self-employed' 'unemployed' 'housemaid''student')

3 marital|object|marital status('married' 'single' 'divorced')

4 education|Object|education background('tertiary' 'secondary' 'unknown' 'primary')

5 default|object|has credit in default('no' 'yes')

6 balance|int64|Balance of the individual

7 Housing|object|has housing loan('no' 'yes')

8 Loan|object|has a personal loan('no' 'yes')

9 contact|object|Contact communication type('unknown' 'cellular' 'telephone')

10 day|int 64|last contact day of week('mon'-'fri')

11 month|object|last contact month of year('may' 'jun' 'jul' 'aug' 'oct' 'nov' 'dec' 'jan' 'feb' 'mar' 'apr' 'sep')

12 duration|int64|last contact duration in seconds

13 campaign|int64|number of contacts performed during this campaign

14 previous|int64|number of contacts performed during this campaign for this client

15 poutcome|object|outcome of the previous marketting campaign('unknown' 'failure' 'other' 'success')

Label

16 deposit|object|has the client subscribed a term deposit('no' 'yes')

Data Analysis

1 Find Unwanted Columns

2 Find Missing Values

3 Find Features with one value

4 Explore the Categorical Features

5 Find Categorical Feature Distribution

6 Relationship between Categorical Features and Label

7 Explore the Numerical Features

8 Find Discrete Numerical Features

9 Relation between Discrete numerical Features and Labels

10 Find Continous Numerical Features

11 Distribution of Continous Numerical Features

12 Relation between Continous numerical Features and Labels

13 Find Outliers in numerical features

14 Explore the Correlation between numerical features

15 Find Pair Plot

Feature Engingineering

Drop unwanted features

Handle missing value

Handle categorical features

Handle feature scaling

Remove outliers

As Per DataAnalysis

no missing value found

no feature found with one value

9 categorical features

default feature does not play important role

it seems some outliers found (age, balance, duration, compaign and previous has some outliers)

Conclusion
