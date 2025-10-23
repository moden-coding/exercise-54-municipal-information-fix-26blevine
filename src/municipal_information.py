#!/usr/bin/env python3

from os import sep
import pandas as pd

def main():
    vals = pd.read_csv("src/municipal.tsv", sep="\t")
    
    shape = vals.shape
    print(f"Shape: {shape[0]}, {shape[1]}")
    print("Columns:")
    for col in vals.columns:
        print(col)



if __name__ == "__main__":
    main()
