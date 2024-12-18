#MM
import time
import main_def as md
import sys
sys.setrecursionlimit(10**6)


with open('dataM.txt', 'r', encoding='utf-8') as fin:
    all_rec = []

    for rec in fin:
        rec = rec.strip()

        if not rec:
            continue

        data = rec.split()
        new_record = ' '.join(data)
        all_rec.append(new_record)

if __name__ == '__main__':

    algorithm_names = ["BubbleSort", "InsertionSort", "SelectionSort", "MergeSort", "QuickSort"]
    bu, In, se, me, qu = all_rec, all_rec, all_rec, all_rec, all_rec

    # Bubble Sort
    startB = time.time()
    md.bubblesort(bu)
    endB = time.time()
    b = (endB - startB) * 10**3
    print(f"{algorithm_names[0]} Total time taken {b:.2f} ms")

    # Insertion Sort
    startI = time.time()
    md.InsertionSort(In)
    endI = time.time()
    i = (endI - startI) * 10**3
    print(f"{algorithm_names[1]} Total time taken {i:.2f} ms")

    # Selection Sort
    startS = time.time()
    md.SelectionSort(se)
    endS = time.time()
    s = (endS - startS) * 10**3
    print(f"{algorithm_names[2]} Total time taken {s:.2f} ms")

    # Merge Sort
    startM = time.time()
    md.MergeSort(me)
    endM = time.time()
    m = (endM - startM) * 10**3
    print(f"{algorithm_names[3]} Total time taken {m:.2f} ms")

    # Quick Sort
    startQ = time.time()
    md.QuickSort(qu, 0, len(qu) - 1)
    endQ = time.time()
    q = (endQ - startQ) * 10**3
    print(f"{algorithm_names[4]} Total time taken {q:.2f} ms")

    # Store time with algorithm name
    total_time = [
        (b, algorithm_names[0]),
        (i, algorithm_names[1]),
        (s, algorithm_names[2]),
        (m, algorithm_names[3]),
        (q, algorithm_names[4])
    ]

    # Sort from most to least
    total_time.sort(key=lambda x: x[0], reverse=True)

    print("\nArrange the time the algorithm takes to do from most to least:")
    for t in total_time:
        print(f"{t[1]}: {t[0]:.2f} ms")

    print(f"\nTakes the most time: {total_time[0][1]} ({total_time[0][0]:.2f} ms)")
    print(f"Take a medium time: {total_time[len(total_time)//2][1]} ({total_time[len(total_time)//2][0]:.2f} ms)")
    print(f"Takes the least time: {total_time[-1][1]} ({total_time[-1][0]:.2f} ms)")
