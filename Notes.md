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

- PCA   主成分分析
- LDA  线性判别分析
- 小波变换
- 离散傅里叶变换



# **Bayes & Decision Tree Classifiers**

## Classification

Definition

- Classification is one of the fundamental skills for survival.
- A kind of **supervised** learning



## **Bayes Theorem**

![](https://p.ipic.vip/w0k4p3.png)



![](https://p.ipic.vip/93hd3o.png)

分析：https://zhuanlan.zhihu.com/p/26262151



## **Decision Making**

- Rules can be easily extracted from the built tree.
- One dataset, many possible trees
- Simpler trees are generally preferred



![](http://pic.guoyaohua.com/image/decision-tree/decision-tree-tutorial-animated3.gif)



### ID3

Iterative Dichotomizer 3

One of the most influential Decision Trees models



### **Entropy**

熵



Gain   信息增益  越大越好，表示降低了不确定性

![](https://p.ipic.vip/halttt.png)









### Overfiting

**Definition**

Given a hypothesis space *H*, a hypothesis *h* ∈ *H* is said to overfit the training data if there exists some alternative hypothesis *h*' ∈ *H*, such as *h* has smaller error than *h*' over the training samples, but *h*' has a smaller error than *h* over the entire distribution of instances.





### Example for ID3

**ID3算法流程**

输入：数据集D，特征集A

输出：ID3决策树

- 对当前样本集合计算出所有属性信息的信息增益
- 先选择信息增益最大的属性作为测试属性，将测试属性相同的样本转化为同一个子样本
- 若子样本集的类别属性只含有单个属性，则分支为叶子节点，判断其属性值并标上相应的符号，然后返回调用处，否则对子样本递归调用本算法。

#### 数据集D

![](https://ask.qcloudimg.com/http-save/yehe-1729674/isyjj5kjaq.png)



#### 特征集A

| Attribute1  考试成绩 A~1~ | 通过考试 | 没有通过考试 |
| ------------------------- | -------- | ------------ |
| 优   D~1~                 | 2/10     | —            |
| 良   D~2~                 | 2/10     | —            |
| 及格   D~3~               | 3/10     | 1/10         |
| 不及格   D~4~             | —        | 2/10         |



| Attribute2  作业完成情况 A~2~ | 通过考试 | 没有通过考试 |
| ----------------------------- | -------- | ------------ |
| 优                            | 2/10     | —            |
| 良                            | 3/10     | —            |
| 及格                          | 1/10     | 1/10         |
| 不及格                        | 1/10     | 2/10         |



| Attribute3  出勤率 A~3~ | 通过考试 | 没有通过考试 |
| ----------------------- | -------- | ------------ |
| 高                      | 7/10     | —            |
| 低                      | —        | 3/10         |



#### 过程

![](https://ask.qcloudimg.com/http-save/yehe-1729674/wyqutrg01i.png)



注：

H(D~1~) = $- \frac{2}{2} \times \log_{2}{\frac{2}{2} } - \frac{0}{0}\times \log_{2}{\frac{0}{0} }  $ = 0

H(D) 针对的是整个数据集，所以分母是10

H(D~1~)针对的是数据集D~1~，整个集合中只有2个元素，所以分母是2



### Example for C4.5

![](https://ask.qcloudimg.com/http-save/yehe-1729674/ztox8uu9wm.png)



