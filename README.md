Project Objective-To build a tool that computes Value at Risk (VaR) for a portfolio using three methods:
Parametric (Variance-Covariance)
Historical Simulation
Monte Carlo Simulation
The project showcases practical risk management techniques, compares results across models, and provides visualizations for deeper insights into portfolio market risk.
Methodology -
Load Portfolio Data – Import historical price data for portfolio assets and their weights.
Data Preprocessing – Calculate daily returns, clean missing values, and standardize data formats.
Parametric VaR –Assume returns follow a normal distribution.
Compute portfolio mean and standard deviation.
Calculate VaR at chosen confidence level (e.g., 95%, 99%).
Historical Simulation –Use actual historical return distribution.
Identify the percentile loss corresponding to the confidence level.
Monte Carlo Simulation –Generate thousands of random return scenarios using statistical properties of the data.
Estimate VaR from simulated loss distribution.
Comparison of Methods – Present differences between the three VaR approaches.
Visualization – Plot loss distributions, VaR thresholds, and method comparisons using matplotlib or seaborn
Conclusion-
This project provides a comprehensive framework for computing VaR using three widely accepted approaches. By applying statistical modeling, simulation techniques, and market risk metrics, it allows portfolio managers, risk analysts, and FRM candidates to:Compare risk estimates under different assumptions.
Skills Showcased -
Statistical Modeling – Variance-covariance approach
Simulation – Monte Carlo scenario generation
Market Risk Metrics – VaR at multiple confidence levels
Data Visualization – matplotlib, seaborn
Better understand portfolio loss potential under normal and stressed conditions.

Enhance decision-making through clear visualizations.
