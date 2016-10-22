import csv
# readcsv_filename = "input_data.csv"

def readcsvfile(readcsv_filename):
    '''
    # first para: filename
    2nd para: r-read mode, w-writemode, a-append(do not overwrite)
    
    '''
    scoreList = []
    with open(readcsv_filename,"r") as scorefile:
        
        scorefile_reader = csv.reader(scorefile)
        
        for row in scorefile_reader:
            if len(row) != 0:
                scoreList = scoreList + [row]
        # print len(scoreList)
                                
    scorefile.close()
    return scoreList

if __name__ == '__main__':
    readcsvfile(readcsv_filename)