 elif(w==2):
  score = float(input("Enter Score: "))
  if score>=0.9 and score<=1:
    grade="A"
  if score>=0.8 and score<0.9:
    grade="B"
  if score>=0.7 and score<0.8:
    grade="C"
  if score>=0.6 and score<0.7:
    grade="D"
  if score<0.6 and score>=0:
    grade="F"
  elif score<0 or score>1:
    print("Enter Valid Score.")
  print(grade)
else:
  print("Enter Valid Choice.")