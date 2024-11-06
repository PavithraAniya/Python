student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")

+++++++++++++++++++++++++

# Input a list of student scores
student_scores = input().split()
max_score = 0
score_check = 0
for score in range(0, len(student_scores)):
  student_scores[score] = int(student_scores[score])
  score_check = student_scores[score]
  #  print(score_check)
  if max_score > score_check:
    max_score = max_score
  else:
    max_score = score_check
print(f"The highest score in the class is: {max_score}")

# Write your code below this row 👇
