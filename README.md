# Benford's Law
Script scans and compares a public financial statement with Benford's distribution. Type in a stock ticker followed by the type of financial statement
you would like to look at (cf=cash flow, bs=balance sheet, is=income statement) and a Kolmogorov-Smirnov test will compare
how the digits in the financial statement differ from Benford's distribution.

<h2>Benford's distribution of digits</h2>
Due to a counting system structured in the base of 10, digits closer to 1 appear more frequently rather than being equally distributed. Benford's law demonstrates this phenomenon in everything from Newton's gravitational constant to financial accounting statements.

![benford1](https://github.com/v-for-vasya/Benfords-law/blob/master/img/benford1.png)

Comparing Benford's distribution with Enron's last financial statement showing clear mismatch in digit distribution
![benford2](https://github.com/v-for-vasya/Benfords-law/blob/master/img/benford2.png)


Example with AMD's cash flow statement by running <code> benford_compare("AMD","cf")</code> in benfords_law.py
![benford3](https://github.com/v-for-vasya/Benfords-law/blob/master/img/benford3.png)
