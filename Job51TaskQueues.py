# coding:utf-8
from Queue import Queue

#class Job51TaskQueues():
#招聘信息查询结果 页数
jobListPageSize=100

#d第一步 使用查询结果页数填充 队列
jobListPageUrlQueue = Queue()
#第二部 下载每页查询结果
jobListPageQueue = Queue()
#第三部 解析每页查询结果 获取职位 URL
jobInfoPageUrlQueue = Queue()
#第四步 下载职位信息页面
jobInfoPageQueue = Queue()
#第五步 解析职位页面
jobInfoBeanQueue = Queue()
#第六部 入库