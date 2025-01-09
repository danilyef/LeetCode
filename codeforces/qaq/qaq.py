##### CODE FORCE
############### PYTHON

s = input()

qaq = 0
qa = 0
q = 0

for i in range(len(s)):
    if s[i] == "Q":
        q +=1
    
    if s[i] == "A":
        qa += q

    if s[i] == "Q" and qa > 0:
        qaq += qa

print(qaq)

