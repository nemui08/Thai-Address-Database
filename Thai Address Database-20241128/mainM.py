#mm
import time
import main_def as md
import sys
sys.setrecursionlimit(10**6)


with open('dataM.txt', 'r', encoding='utf-8') as fin:
    AllRecord = []

    for Record in fin:

        Record = Record.strip()
        if not Record:
            continue

        Data = Record.split()
        NewRecord = ' '.join(Data)
        AllRecord.append(NewRecord)
        
if __name__ == '__main__':
    Bubble = list(AllRecord) 
    Insert = list(AllRecord)
    Select = list(AllRecord)
    Merge = list(AllRecord)
    Quick = list(AllRecord)
    
    start_b = time.time()    
    md.bubblesort(Bubble)
    end_b = time.time()
    b = (end_b-start_b) * 10**3
    print("bubblesort total time taken is ", b ,"milliseconds")
    time_bubble = b
    print()
    
    start_i = time.time()    
    md.InsertionSort(Insert)
    end_i = time.time()
    i = (end_i-start_i) * 10**3
    print("insertionSort total time taken is ", i ,"milliseconds")
    time_insert = i
    print()
    
    start_s = time.time()    
    md.SelectionSort(Select)
    end_s = time.time()
    s = (end_s-start_s) * 10**3
    print("SelectionSort total time taken is ", s ,"milliseconds")
    time_select = s
    print()
    
    start_m = time.time()    
    md.MergeSort(Merge)
    end_m = time.time()
    m = (end_m-start_m) * 10**3
    print("MergeSort total time taken is ", m ,"milliseconds")
    time_merge = m
    print()
    
    start_q = time.time()    
    md.QuickSort(Quick,0 ,len(Quick)-1)
    end_q = time.time()
    q = (end_q-start_q) * 10**3
    print("QuickSort total time taken is ", q ,"milliseconds")
    time_quick = q
    print()
    
    TotalTimes = [time_bubble, time_insert, time_select, time_merge, time_quick]

    md.bubblesortLOW(TotalTimes)
    
    print(TotalTimes[0])
    a = input("Please enter the algorithm name. You can check it from above. Enter , before entering the name = ")
    TotalTimes[0] = f"{TotalTimes[0]}{a}"

    print(TotalTimes[1])
    b = input("Please enter the algorithm name. You can check it from above. Enter , before entering the name = ")
    TotalTimes[1] = f"{TotalTimes[1]}{b}"

    print(TotalTimes[2])
    c = input("Please enter the algorithm name. You can check it from above. Enter , before entering the name = ")
    TotalTimes[2] = f"{TotalTimes[2]}{c}"

    print(TotalTimes[3])
    d = input("Please enter the algorithm name. You can check it from above. Enter , before entering the name = ")
    TotalTimes[3] = f"{TotalTimes[3]}{d}"

    print(TotalTimes[4])
    e = input("Please enter the algorithm name. You can check it from above. Enter , before entering the name = ")
    TotalTimes[4] = f"{TotalTimes[4]}{e}"
    
    print("Sort the time the Algorithm takes to do a task from most to least.", TotalTimes)
    print()
    print("Takes the most time is ", TotalTimes[-1])
    print()
    print("Takes the least amount of time is ", TotalTimes[0])
    print()
    print("Take a medium time is ", TotalTimes[2])
    