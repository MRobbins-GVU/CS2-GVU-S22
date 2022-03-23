import time

def sum_of_n(n):
    start = time.time()
    
    #sum
    total = 0
    for i in range(1, n+1):
        total += i
    
    #end time
    end = time.time()
    
    runtime = end - start
    
    #return sum, end-start
    return total, runtime

def sum_of_n_2(n):
    start = time.time()
    temp = 0
    total = 0
    for i in range(1, n+1):
        temp = total + i
        total = temp

    end = time.time()
    runtime = end - start
    
    return total, runtime
    
def main():
    # print(sum_of_n(10000))
    print(sum_of_n(100000))
    print(sum_of_n_2(100000))
    print(sum_of_n(1000000))
    print(sum_of_n_2(1000000))
    print(sum_of_n(5000000))
    print(sum_of_n_2(5000000))
    #print(sum_of_n(10000000))
    
main()

# Results from my home computer
# (5000050000, 0.0043621063232421875)
# (500000500000, 0.04368114471435547)
# (12500002500000, 0.2192237377166748)
