import sys as s

sys = "반복 시스템입니다."

while True:
    print(sys)
    sys = s.stdin.readline().rstrip()
    if sys == "exit":
        break
print("종료합니다.")
