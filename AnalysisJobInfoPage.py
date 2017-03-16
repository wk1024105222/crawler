# coding:utf-8
import logging
import os
import Job51Util
import MyThread
import time
import Job51Driver
import SaveJobInfoToDB

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(thread)d [%(threadName)s] %(filename)s %(module)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='log/AnalysisJobInfoPage.log',
                filemode='a')

class AnalysisJobInfoPage(MyThread.MyThread):
    def run(self):
        emptyNum=0
        while True:
            time.sleep(self.requestWait)
            if self.inQueue.empty():
                if emptyNum>10:
                    # 连续50次 empty 退出
                    logging.info('emptyNum > 10 thread stop')
                    break
                emptyNum+=1
                # logging.info('AnalysisJobInfoPage inQueue is empty wait for '+str(self.emptyWait)+'s')
                time.sleep(self.emptyWait)
                continue
            emptyNum=0
            jobInfoPageFile = self.inQueue.get()
            if super(AnalysisJobInfoPage, self).whetherDone(jobInfoPageFile.split('/')[-1][0:8]):
                continue

            jobBean = Job51Util.getJobInfoFromHtml(jobInfoPageFile)['jobbean']
            self.outQueue.put(jobBean)

            logging.info('[jobInfo'+jobBean.code+ '] Analysis successed filepath:'+jobInfoPageFile)
        return

    def fillInQueue(inQueue):
        for filename in os.listdir(Job51Driver.jobInfoPath):
            inQueue.put(Job51Driver.jobInfoPath+'/'+filename)

    def fillDoneQueue(doneQueue):
        SaveJobInfoToDB.SaveJobInfoToDB.fillDoneQueue(doneQueue)
