import pandas as pd 
# making data frame 
df = pd.read_csv("C:\Users\harsh parab\Documents\python\Learning_python-main\Hello.csv") 
ser = pd.Series(df['Roll No']) 
print(ser)
ser = pd.DataFrame(df[['Roll No.','Name']]) 
print(ser)