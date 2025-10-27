!pip install psutil --quiet

import numpy as np
import time
import psutil
import sys

N = 2000 

def print_stage(stage, bar=0, cpu=0):
    stages = {
        "NEW":        "NEW        | Yaratilmoqda...",
        "READY":      "READY      | Kutishga tayyor...",
        "RUNNING":    f"RUNNING    | Hisoblanmoqda...  [{bar*'▓'}{(50-bar)*'░'}]  CPU: {cpu:4.1f}%",
        "WAITING":    "WAITING    | Kutilmoqda (pauza)...",
        "TERMINATED": "TERMINATED | Jarayon tugadi"
    }
    sys.stdout.write("\r" + stages[stage])
    sys.stdout.flush()

# --- NEW ---
print_stage("NEW")
time.sleep(1.2)
A = np.random.rand(N, N)
B = np.random.rand(N, N)
np.savetxt("matrix_A.txt", A, fmt="%.5f")
np.savetxt("matrix_B.txt", B, fmt="%.5f")

# --- READY ---
print_stage("READY")
time.sleep(1.2)
print() 
bar_steps = 50

# --- RUNNING 1 ---
for i in range(bar_steps + 1):
    cpu = psutil.cpu_percent(interval=0.15)
    step1 = np.dot(A, B.T) 
    print_stage("RUNNING", i, cpu)
print("\n")
time.sleep(0.8)

# --- WAITING ---
print_stage("WAITING")
time.sleep(2)
print()

# --- RUNNING 2 ---
for i in range(bar_steps + 1):
    cpu = psutil.cpu_percent(interval=0.15)
    result = np.dot(step1, B) 
    print_stage("RUNNING", i, cpu)
np.savetxt("result.txt", result, fmt="%.5f")
print("\n")
time.sleep(1)

# --- TERMINATED ---
print_stage("TERMINATED")
print("\n All done!")
print("\n Quyidagi fayllar saqlandi:")
print("- matrix_A.txt")
print("- matrix_B.txt")
print("- result.txt")
