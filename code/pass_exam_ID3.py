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