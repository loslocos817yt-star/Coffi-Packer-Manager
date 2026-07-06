import sys
import math

# Uso: FuckEngland(suma 2,2) -> var
comando_completo = sys.argv[1].split(" ")
op = comando_completo[0]
nums = comando_completo[1].split(",")

if op == "suma":
    print(float(nums[0]) + float(nums[1]))
elif op == "resta":
    print(float(nums[0]) - float(nums[1]))
elif op == "div":
    print(float(nums[0]) / float(nums[1]))
elif op == "pot":
    print(pow(float(nums[0]), float(nums[1])))
elif op == "raiz":
    print(math.sqrt(float(nums[0])))
  
