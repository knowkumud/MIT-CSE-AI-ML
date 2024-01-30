#!/usr/bin/env python
# coding: utf-8

# <p style="text-align: center;"> 
# WEEK 1</p>

# # 1. Write a PySpark program to square set of integers 

# In[5]:


import os
import sys
import pyspark 
#from pyspark import SparkContext 

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


# In[8]:


from pyspark.sql import SparkSession 
# Create a SparkSession
spark = SparkSession.builder.appName("SquareNumbers").getOrCreate()

# List of numbers
numbers = [2,3,5,7]

# Creating DataFrame from the list
df = spark.createDataFrame([(num,) for num in numbers], ["numbers"])

# Squaring each number using DataFrame operations
squared_df = df.withColumn("squared_numbers", df["numbers"] ** 2)

# Showing the DataFrame with squared numbers
squared_df.show()

# Stop SparkSession
spark.stop()


# # 2. Write a PySpark program to find the maximum of given set of numbers.

# In[11]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import max as max_

# Create a SparkSession
spark = SparkSession.builder.appName("Maximum").getOrCreate()

# List of numbers
numbers = [49,9,64,25,81,90,36]

# Create a DataFrame from the list
df = spark.createDataFrame([(num,) for num in numbers], ["numbers"])

# Find the maximum number using DataFrame operations
max_number = df.agg(max_("numbers")).collect()[0][0]

# Print the maximum number
print("Maximum number:", max_number)

# Stop SparkSession
spark.stop()


# # 3.Write a PySpark program to find average of N numbers.

# In[18]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
spark = SparkSession.builder.appName("AverageOfNumbers").getOrCreate()
numbers = [100, 25, 2, 88, 72, 97, 12, 9]
df = spark.createDataFrame([(num,) for num in numbers], ["numbers"])
average = df.agg(avg("numbers")).collect()[0][0]

# Print the average
print("Average:", average)

# Stop SparkSession
spark.stop()


# # 4. Demonstrate how to read a CSV file into a PySpark DataFrame.
# # 5 Use PySpark commands to display the first few rows and schema of a DataFrame.
# # 6 Calculate basic summary statistics for a specific column in the DataFrame.

# In[21]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName("Summary").getOrCreate()

# Read the CSV file into a DataFrame
file_path = "week1.csv"  # Replace with your file path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
df.show()

# Display the schema of the DataFrame
print("DataFrame schema:")
df.printSchema()

# Calculate basic summary statistics for the 'salary' column
print("Summary statistics for the 'salary' column:")
salary_stats = df.select("Subjects").summary("count", "min", "max", "mean", "stddev")
salary_stats.show()

# Stop SparkSession
#spark.stop()


# In[ ]:




