Salary Prediction Using Linear Regression
Overview

This project analyzes the relationship between Years of Experience and Salary using simple linear regression. The goal is to predict an employee’s salary based on their experience.

Dataset

The dataset contains 30 records with the following columns:

YearsExperience	Salary
1.2	39344
1.4	46206
1.6	37732
...	...
10.6	121873

YearsExperience: Number of years an employee has worked.

Salary: Annual salary of the employee in dollars.

Model

A linear regression model was used to fit the data, which assumes a linear relationship between experience and salary.

The resulting regression equation is:

Salary
=
(
Slope
)
×
YearsExperience
+
(
Intercept
)
Salary=(Slope)×YearsExperience+(Intercept)

Where:

Slope = 9423.82 → Salary increases by approximately $9,424 for each additional year of experience.

Intercept = 24,380.20 → Estimated starting salary (at 0 years of experience).

Prediction

Using the model, the predicted salary for an employee with 8 years of experience is:

Salary
=
94
,
423
×
8
+
24
,
380
≈
99
,
771
Salary=94,423×8+24,380≈99,771
Model Performance

The R² score measures how well the model explains the variation in the data:

R² Score (Test Data) = 90.24%

This indicates that approximately 90% of the variance in salaries can be explained by years of experience. The model fits the data reasonably well, but there are some deviations due to irregular salary jumps.

Conclusion

The linear regression model provides a good estimate of salary based on years of experience.

It predicts salaries reasonably well for employees with typical experience levels.

Some variations in actual salaries suggest factors beyond experience may influence pay.
