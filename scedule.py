import schedule
import time

def job1():
    print("I'm working... 1")
def job2():
    print("I'm working... 2")

schedule.every(1).seconds.do(job1)
schedule.every(1).minutes.do(job2)


while True:
    schedule.run_pending()
    time.sleep(1)