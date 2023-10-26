**House_Price_Prediction**

This is the first project I had used a house prices dataset to predict the housing prices. I loaded the dataset using pandas. I have performed EDA using Jupyter Notebook IDE and using Matplotlib and Seaborn library of python. While performing the EDA, I had performed below EDAs

1. Univariate Analysis
2. Bivariate Analysis
3. Multivariate Analysis

**Univariate Analysis:**

Here I had applied a pie chart and countplot on the categorical data to check the values of each label in these features. I had used a for loop and applied it on dataset categorical data columns.

**Mainroad:**

85.9% houses are touching the mainroad and only 14.1% are not touching the mainroad. The same is shown in the pie chart. As the countplot is showing almost 470 Houses are touching mainroad and only 75 houses are not on mainroad.

**Guestroom:**

82.2% houses doesn’t have a guestroom whereas 17.8% houses have it. The same is shown in the pie chart. As the countplot is showing almost 450 Houses doesn’t have a guestroom, whereas approximately 95 houses does have it.

**Basement:**

65% houses doesn’t have a basement whereas 35% houses have it. The same is shown in the pie chart. As the countplot is also showing almost 355 Houses doesn’t have a basement, whereas approximately 190 houses does have it.

**HotWaterHeating:**

95.4% houses doesn’t have HotWaterHeating facility, whereas only 4.6% houses have it. The same is shown in the pie chart. The countplot is also showing almost 520 Houses doesn’t have HotWaterHeating facility, only 25 houses have it.

**Airconditioning:**

68.4% houses does have an Air_Conditioning installed, whereas 31.6% doesn't. The same is shown in the pie chart. As the countplot is showing almost 375 Houses have Air_Conditioning installed, whereas approximately 170 houses doesn’t have it.

**Furnishing_Status:**

41.7% houes are furnished, 32.7% are semi-furnished, whereas 25.7% are unfurnished. The same is shown in the pie chart. The countplot is approximately 230 houes are furnished, approxx 180 are semi-furnished, whereas approximately 135 houses are unfurnished.

**Bedroom:**

In our dataset. maximum houses have 4 bedrooms, which takes 55% of total houses. At second place we have the demand of 3 Bedroom houses and then 5 bedroom. 1, 2 and 6 bedroom demands were too low.

**Bathrooms:**

In our dataset. maximum houses have 2 bathrooms, which takes 73.6% of total houses. At second place we have the demand of 4 bathrooms houses. Demand for 1 and 3 bathroom houses were too low.

**Stories:**

Majority of the customeres have preferred 3 & 4 story houses, which conclude almost 85% people went for 3 and 4 story houses. Demand for 1 and 2 story houses were too low.

**Parking:**

Majority of the customeres have preferred at least 2 OR 3 parking spaces in their house, which include almost 78% of the people went for 2 and 3 parking spaces. There are people who went for house with 0 parking space. Whereas only 2.2% of the people selected at least 1 parking space in their house.

**Price:**

Majority of the customers purchased the house between 3.5 Million to (almost) 6 Million. 

**Area:**

Majority of the customers purchased the house which has the area betwen 3500 SQFT - 7000 SQFT.

**Bivariate Analysis:**

I have used pairplot to perform bivariate analysis.
Along with this, I had also used groupby method of pandas to check the different parameters of the dataset with respect to Area and Price.

**Bedroom vs area vs price:**

By checking the bedroom with mean value of area and price, I found that 1 Bedroom housee has taken an area of approxx 3600 SQFT, whereas the prces for it is in the range of 2.7 - 2.8 M. 2 Bedroom house has the average area of 4500 SQFT annd the price range is 3.6 M. 3 Bedroom house has an average area of 5200 SQFT, whereas the price for it in the range of 5M (Approx). 4 Bedroomm house has an aread of 5500 SQFT, whereas the prices for this is 5.7 M (Approxx), 5 Bedroom house has the average area above 6K SQFT, wheras the prices for it in the range of 5.8-5.9 M, 6 Bedroom houses are built on an average area of 3800 SQFT, whereas the price for it lies around 5M.

**Bathrooms vs area vs price:**

The house having 1 bathroom has an average area of 4800 SQFT and the price range for this is around 4M. 2 bathroom house are having an average area of around 6K SQFT and prices in the range of 6M, 3 Bathroom house have an area of around 6700 SQFT, whereas the price is in the range of 7.5M, 4 Bathrroom house are built on around 9500 SQFT area, whereas the price is highest of around 12M.

**Stories vs area vs price:**

Majority of the house built with 1 story have an area around 5200 SQFT, wheereas the 2 story houses have 4800 SQFT, the price for 1 Sotry house is ranign 4M, whereas for  story it is around 4.8M. 3 Story houses are havin an area of 5300 SQFT with the pricce range of 5.8M, 4 story house are occupying the highest area with higher price, the area is 6500+ whereas the price is 7.4M+.

**Mainroad vs area vs price:**

Houses bulit on an average area of 3500, the mainroad connectivity is not there and price range of house with no mainroad connectivity is around 3.5M, whereas the houses having mainroad connectivity have an average area of 5300 with the price rangin 5M+.

**Multivariate Analysis:**

I had checked the coorelation of the data to understand the dependancy.

This is the very first project I was working on. The data is clean. There are no missing values. Hence, I directly converted the categorical feature values to numerical values using  the replace method of pandas. I had also used get_dummies method of pandas to convert the furnishingstatus feature of the dataset.

I wrote this code using main method. I have created a class **data_import** and stored the path in main method. Later I loaded it using pandas in constructor. I had also kept my regression algorithm in cnstructor. 
I have created a preprocessing  function to preprocess the data. I also splited the data in this function only.

I created a **data_split** function to separate the dependent and independent feature. I created two separate functions to train and test the model i.e. **training_modal & test_modal** respectively.
