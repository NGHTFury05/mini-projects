#This is a simple python cli tool that analyzes text files for detailed summaries.
import sys
import pandas as pd
def main():
    if len(sys.argv)>1:
        filepath=sys.argv[1]
        analyze(filepath)
    else:
        print("Usage: python analyze.py <file_path>")
        return
    
def analyze(fp):
    df=pd.read_csv(fp)
    summary=df.describe()
    print("Data Summary:")
    print(summary)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nLast 5 Rows:")
    print(df.tail())
if __name__=="__main__":
    main()