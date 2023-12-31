# Data Preprocessing

**Major Tasks in Data Preprocessing**

- Data cleaning
  - Fill in missing values, smooth noisy data, identify or remove outliers, and resolve inconsistencies
- Data integration
  - Integration of multiple databases, data cubes, or files
-  Data transformation
  - Normalization and aggregation
- Data reduction
  - Obtains reduced representation in volume but produces the same or similar analytical results 
- Data discretization
  - Part of data reduction but with particular importance, especially for numerical data



## Data Cleaning

### **Why Data Preprocessing?**

- Real data are dirty.
  - The biggest challenge in many data mining projects
- Incomplete
- Noisy
- Inconsistent
- Redundant



**Missing Data**

- Data are not always available.
- Different reasons and types.



**How to handle missing data?**

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



### Attribute

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





# Classification – Decision Trees

## Classification

- Definition

  - A kind of **supervised** learning



## **Decision Making**

- Rules can be easily extracted from the built tree.
- One dataset, many possible trees
- Simpler trees are generally preferred



![](http://pic.guoyaohua.com/image/decision-tree/decision-tree-tutorial-animated3.gif)



**ID3**

- Full name : Iterative Dichotomizer 3


- One of the most influential Decision Trees models




**信息量**

- 信息量在是作为信息“多少”的度量，这里的信息就是你理解的信息，比如一条新闻，考试答案等等

- 当越不可能的事件发生了，我们获取到的信息量就越大。越可能发生的事件发生了，我们获取到的信息量就越小

- 如已知事件Xi已发生，则表示Xi所含有或所提供的信息量：

  - ![](https://ask.qcloudimg.com/http-save/yehe-1729674/glt8fc5w9d.png)

  - 如果是以2为底数，单位是bit；如果以e为底数，单位是nat；如果以10为底数，单位是det；

    例如，今天下雨的概率是0.5，则包含的信息量为 ：$- \log_{2}{0.5} = 1$



**Entropy**   熵

- 熵（Entropy）是接受信息量的平均值，用于确定信息的不确定程度，是随机变量的均值。信息熵越大，信息就越凌乱或传输的信息越多，熵本身的概念源于物理学中描述一个热力学系统的无序程度。信息熵的处理信息是一个让信息的熵减少的过程。

- 假设X是一个离散的随机变量，且它的取值范围为x~1~,x~2~,…,x~n~，每一种取到的概率分别是 p~1~,p~2~,…,p~n~，那么 X 的熵定义为:

  ![](https://ask.qcloudimg.com/http-save/yehe-1729674/yfjmaaq3hx.png)



**Gain**   信息增益  

- 越大越好，表示降低了不确定性
- ![](https://ask.qcloudimg.com/http-save/yehe-1729674/to6z26uucj.png)



**Overfiting**

- Definition
  - Given a hypothesis space *H*, a hypothesis *h* ∈ *H* is said to overfit the training data if there exists some alternative hypothesis *h*' ∈ *H*, such as *h* has smaller error than *h*' over the training samples, but *h*' has a smaller error than *h* over the entire distribution of instances.



## Example for ID3

**ID3算法流程**

输入：数据集D，特征集A

输出：ID3决策树

- 对当前样本集合计算出所有属性信息的信息增益
- 先选择信息增益最大的属性作为测试属性，将测试属性相同的样本转化为同一个子样本
- 若子样本集的类别属性只含有单个属性，则分支为叶子节点，判断其属性值并标上相应的符号，然后返回调用处，否则对子样本递归调用本算法。

### Data set	

数据集D

![](https://ask.qcloudimg.com/http-save/yehe-1729674/isyjj5kjaq.png)



### Attribute set

特征集A / 属性集A

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



### Progress	

![](https://p.ipic.vip/zfjotm.png)



注：

H(D~1~) = $- \frac{2}{2} \times \log_{2}{\frac{2}{2} } - \frac{0}{0}\times \log_{2}{\frac{0}{0} }  $ = 0

H(D) 针对的是整个数据集，所以分母是10

H(D~1~)针对的是数据集D~1~，整个集合中只有2个元素，所以分母是2



### Code

[pass_exam_ID3.py](./code/pass_exam_ID3.py)

```python
from math import log
def createDataSet():
    # 考试成绩 score :优:1, 良:2, 及格:3, 不及格:4
    # 作业完成情况 assignment :优:1, 良:2, 及格:3, 不及格:4
    # 出勤率 attendance :高:1, 低:2
    # 通过考试 pass :yes, no
    dataSet=[
        [1,1,1,'yes'],
        [1,2,1,'yes'],
        [2,1,1,'yes'],
        [2,2,1,'yes'],
        [3,2,1,'yes'],
        [3,3,1,'yes'],
        [3,4,2,'no'],
        [3,4,1,'yes'],
        [4,3,2,'no'],
        [4,4,2,'no']
    ]
    labels=['score','assignment','attendance','pass']
    return dataSet,labels
def calcShannonEnt(dataSet):
    #返回数据集行数
    numEntries=len(dataSet)
    #保存每个标签（label）出现次数的字典
    labelCounts={}
    #对每组特征向量进行统计
    for featVec in dataSet:
        currentLabel=featVec[-1]#提取标签信息
        if currentLabel not in labelCounts.keys():#如果标签没有放入统计次数
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1#label计数
    shannonEnt=0.0
    #计算经验熵
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries #选择该标签的概率
        shannonEnt-=prob*log(prob,2)            #利用公式计算
        # print("选择该标签的概率为："+ str(prob) )
        # print("对数为："+ str(log(prob,2)) )
    return shannonEnt
def chooseBestFeatureToSplit(dataSet):
    #特征数量
    numFeatures = len(dataSet[0]) - 1
    #计数数据集的香农熵
    baseEntropy = calcShannonEnt(dataSet)
    #信息增益
    bestInfoGain = 0.0
    #最优特征的索引值
    bestFeature = -1
    #遍历所有特征
    for i in range(numFeatures):
        # 获取dataSet的第i个所有特征
        featList = [example[i] for example in dataSet]
        #创建set集合{}，元素不可重复
        uniqueVals = set(featList)
        #经验条件熵
        newEntropy = 0.0
        #计算信息增益
        for value in uniqueVals:
            #subDataSet划分后的子集
            subDataSet = splitDataSet(dataSet, i, value)
            #计算子集的概率
            prob = len(subDataSet) / float(len(dataSet))
            #根据公式计算经验条件熵
            # print("prob为："+ str(prob) )
            # print("ShannonEnt为："+ str(calcShannonEnt((subDataSet))) )
            newEntropy += prob * calcShannonEnt((subDataSet))
        #信息增益
        print("第%d个特征的熵为"% i+str(newEntropy) )
        infoGain = baseEntropy - newEntropy
        #打印每个特征的信息增益
        print("第%d个特征的增益为%.3f" % (i, infoGain))
        print("")
        #计算信息增益
        if (infoGain > bestInfoGain):
            #更新信息增益，找到最大的信息增益
            bestInfoGain = infoGain
            #记录信息增益最大的特征的索引值
            bestFeature = i
            #返回信息增益最大特征的索引值
    return bestFeature
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
if __name__=='__main__':
    dataSet,features=createDataSet()
    print(dataSet)
    print("")
    print("数据集的信息熵为:",str(calcShannonEnt(dataSet)))
    print("")
    print("最优索引值：",str(chooseBestFeatureToSplit(dataSet)))
```





## Example for C4.5

<img src="https://p.ipic.vip/srjayp.png"  />



# **Bayes**



## **Bayes Theorem**

![](https://p.ipic.vip/w0k4p3.png)



![](https://p.ipic.vip/93hd3o.png)

分析：https://zhuanlan.zhihu.com/p/26262151

