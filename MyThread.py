# coding:utf-8
from abc import abstractmethod, ABCMeta
import threading

class MyThread(threading.Thread):
    __metaclass__ = ABCMeta
    """
    从51job下载 职位包含java 的job 每个job以html保存本地
    """
    def __init__(self, inQueue, outQueue, emptyWait, requestWait, doneMap):
        '''
        线程基类
        :param inQueue: 数据输入队列
        :param outQueue: 数据输出队列
        :param emptyWait: 输入队列为空时等待时间 单位s
        :param requestWait: 网页请求 间隔时间 单位s
        :return:
        '''
        threading.Thread.__init__(self)
        self.inQueue = inQueue
        self.outQueue = outQueue
        self.emptyWait = emptyWait
        self.requestWait = requestWait
        self.doneMap = doneMap

    def whetherDone(self,key):
        return key in self.doneMap

    # # 填充 数据输入队列
    # @abstractmethod
    # @staticmethod
    # def fillInQueue(inQueue):pass
    #
    # # 填充已完成的队列 用于过滤 输入队列已完成的数据
    # @staticmethod
    # @abstractmethod
    # def fillDoneQueue(doneQueue):pass
