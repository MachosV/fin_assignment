import pandas as pd
import time
import sqlite3
import os

def calculateNumberOfCSVRows(infile,chunksize):
    numberOfRows = 0
    df = pd.read_csv(infile, chunksize=chunksize)
    for chunk in df:
        for row in chunk.iterrows():
            numberOfRows += 1
    del df
    return numberOfRows

def main():
    infile = "H:/data/requests/requests_Combined_Featureless_Shuffled_v2.csv"
    chunksize = 256
    processedCounter = 0
    totalRows = calculateNumberOfCSVRows(infile, chunksize)
    db = sqlite3.connect("test.sqlite3")
    db.execute("create table items(description)")
    df = pd.read_csv(infile, chunksize=chunksize)
    start_time = time.time()
    for chunk in df:
        chunk_start_time = time.time()
        data = []
        for row in chunk.iterrows():
            data.append((row[1].values[0],))
            processedCounter+=1 #first column contains data
        #bulk insert the rows in the data
        db.executemany("insert into items(description) values (?)", data)
        db.commit()
        del data
        os.system("cls")
        print("--- %s seconds ---" % (time.time() - chunk_start_time))
        print("Processed:",processedCounter,"of",totalRows)
        print("{:.2f}% complete".format(processedCounter*100/totalRows))
    os.system("cls")
    print("100% Complete")
    print("Processed:",processedCounter,"of",totalRows)
    print("--- %s seconds ---" % (time.time() - start_time))
    print ("Exiting") 
    db.close()

if __name__ == "__main__":
    main()