# Data Preprocessing

## Data Cleaning

### **Why Data Preprocessing?**

- Real data are dirty!
  - The biggest challenge in many data mining projects
- Incomplete
- Noisy
- Inconsistent
- Redundant



**Missing Data**

- Data are not always available.
- Different reasons and types.



### **How to handle missing data?**

- Ignore
- Fill in the missing values manually
- Fill in the missing values automatically
- More art than science.    没有特别严格或学术化的规定



**Outlier**

离群值



**Duplicate Data**

1. Create keys
2. Sort
3. Merge



## Data Transformation

Now we have an error free dataset, but data still needs to be standardized.



**Attribute Types**

- Continuous.  连续的，例如实数
- Discrete   离散的，例如整数
- Ordinal    顺序，例如好、中、坏
- Nominal   名词性的，例如红绿蓝
- String



**Type Conversion**

Need to encode.



**Sampling** (采样) 

- Sampling is applied to reduce the time complexity.
- In statistics, sampling is applied often because obtaining the entire set of data is expensive.
- Sampling can be also used to adjust the class distributions.



### **Normalization**

**Min-max normalization**    

极值正规化

![](https://p.ipic.vip/royqhj.png)



**Z-score normalization** 

μ: mean 平均数, σ: standard deviation. 标准差

![](https://p.ipic.vip/9u21ne.png)



## Data Description



![](https://p.ipic.vip/r3kp6k.png)



### **Data Visualization** 

- 1D
  - Pie chart
  - Bar chart
  - Column chart
- 2D
- Surf Plots 波浪图(3D)
- Box Plots 箱线图 (High Dimensional) 
- Parallel Coordinates  平行坐标(High Dimensional) 
- CiteSpace 科学图谱



## Feature Selection

**Class Distributions**

**Feature Subset Search**    特征子集搜索

- Exhaustive   穷举搜索，排列组合
- branch and bound 分支定界法
- Top K Individual Features
- Sequential Forward Selection
- Sequential Backward Selection
- Optimization Algorithms



## Feature Extraction