import time


total_time = 20
whole_blocks = 50
start_time = time.time()


b = "\u2588"    # █
c = "\u2591"    # ░


print(f"[{whole_blocks*c} Progress Percentage: 0% | Time remaining: 0", end='')


for i in range(0, whole_blocks+1):
    time_remaining = total_time - round(time.time() - start_time)
    progress_percentage = round(i/whole_blocks*100)

    print(f"\r[{i*b}{(whole_blocks-i)*c}] Progress Percentage: {progress_percentage}%"
          f"| Time remaining: {time_remaining}", end='')
    time.sleep(total_time/whole_blocks)


