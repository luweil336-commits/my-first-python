scores = {
  "数学分析": 85,
  "离散数学": 92,
}
def average(s):
  return sum(s.values())/len(s)
def highest(s):
  name=max(s,key=s.get)
  return name,s[name]
def lowest(s):
  name=min(s,key=s.get)
  return name,s[name]
def rank(s):
  return (sorted(s.items(),key=lambda x:x[1], reverse=True))
def count_pass(x):
  n=0
  for score in x:
    if score >= 60:
      n+=1
  return n

print("平均分：", round(average(scores),2))
print("最高分：", highest(scores))
print("最低分：", lowest(scores))
print("及格门数：", count_pass(scores.values()))
print("\n排名：")
for i, (name, score) in enumerate(rank(scores), 1):
    print(f"{i}. {name}：{score}")