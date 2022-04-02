#importing
import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dataFrames = pd.read_csv("StudentsPerformance.csv")

mathscoreList = dataFrames["math score"].to_list()
readingscoreList = dataFrames["reading score"].to_list()
writingscoreList = dataFrames["writing score"].to_list()

#Mean
mathscoreMean = statistics.mean(mathscoreList)
readingscoreMean = statistics.mean(readingscoreList)
writingscoreMean = statistics.mean(writingscoreList)

#Median
mathscoreMedian = statistics.median(mathscoreList)
readingscoreMedian = statistics.median(readingscoreList)
writingscoreMedian = statistics.median(writingscoreList)

#Mode
mathscoreMode = statistics.mode(mathscoreList)
readingscoreMode = statistics.mode(readingscoreList)
writingscoreMode = statistics.mode(writingscoreList)

#Printing Mean, Median and Mode
print("Mean, Median and Mode of Math score is {}, {} and {} respectively".format(mathscoreMean, mathscoreMedian, mathscoreMode))
print("Mean, Median and Mode of Reading score is {}, {} and {} respectively".format(readingscoreMean, readingscoreMedian, readingscoreMode))
print("Mean, Median and Mode of Writing score is {}, {} and {} respectively".format(writingscoreMean, writingscoreMedian, writingscoreMode))

#Standard Deviation
mathscorestdDeviation = statistics.stdev(mathscoreList)
readingscorestdDeviation = statistics.stdev(readingscoreList)
writingscorestdDeviation = statistics.stdev(writingscoreList)

#Printing standard deviation
print("Standard Deviation of Math score is {}".format(mathscorestdDeviation))
print("Standard Deviation of Reading score is {}".format(readingscorestdDeviation))
print("Standard Deviation of Writing score is {}".format(writingscorestdDeviation))

#1, 2 and 3 Standard Deviations for Math score
mathscore1stdDeviationStart, mathscore1stdDeviationEnd = mathscoreMean - mathscorestdDeviation, mathscoreMean + mathscorestdDeviation
mathscore2stdDeviationStart, mathscore2stdDeviationEnd = mathscoreMean - (2 * mathscorestdDeviation), mathscoreMean + (2 * mathscorestdDeviation)
mathscore3stdDeviationStart, mathscore3stdDeviationEnd = mathscoreMean - (3 * mathscorestdDeviation), mathscoreMean + (3 * mathscorestdDeviation)

#1, 2 and 3 Standard Deviations for Reading score
readingscore1stdDeviationStart, readingscore1stdDeviationEnd = readingscoreMean - readingscorestdDeviation, readingscoreMean + readingscorestdDeviation
readingscore2stdDeviationStart, readingscore2stdDeviationEnd = readingscoreMean - (2 * readingscorestdDeviation), readingscoreMean + (2 * readingscorestdDeviation)
readingscore3stdDeviationStart, readingscore3stdDeviationEnd = readingscoreMean - (3 * readingscorestdDeviation), readingscoreMean + (3 * readingscorestdDeviation)

#1, 2 and 3 Standard Deviations for Writing score
writingscore1stdDeviationStart, writingscore1stdDeviationEnd = writingscoreMean - writingscorestdDeviation, writingscoreMean + writingscorestdDeviation
writingscore2stdDeviationStart, writingscore2stdDeviationEnd = writingscoreMean - (2 * writingscorestdDeviation), writingscoreMean + (2 * writingscorestdDeviation)
writingscore3stdDeviationStart, writingscore3stdDeviationEnd = writingscoreMean - (3 * writingscorestdDeviation), writingscoreMean + (3 * writingscorestdDeviation)

#Plotting the graph for Math score
figure = ff.create_distplot([mathscoreList], ["Math Results"], show_hist = False)
figure.add_trace(go.Scatter(x = [mathscoreMean, mathscoreMean], y = [0, 0.17], mode = "lines", name = "MEAN"))

figure.add_trace(go.Scatter(x = [mathscore1stdDeviationStart, mathscore1stdDeviationStart], y = [0, 0.17], mode = "lines", name = "START OF STANDARD DEVIATION 1"))
figure.add_trace(go.Scatter(x = [mathscore1stdDeviationEnd, mathscore1stdDeviationEnd], y = [0, 0.17], mode = "lines", name = "END OF STANDARD DEVIATION 1"))

figure.add_trace(go.Scatter(x = [mathscore2stdDeviationStart, mathscore2stdDeviationStart], y = [0, 0.17], mode = "lines", name = "START OF STANDARD DEVIATION 2"))
figure.add_trace(go.Scatter(x = [mathscore2stdDeviationEnd, mathscore2stdDeviationEnd], y = [0, 0.17], mode = "lines", name = "END OF STANDARD DEVIATION 2"))

figure.add_trace(go.Scatter(x = [mathscore3stdDeviationStart, mathscore3stdDeviationStart], y = [0, 0.17], mode = "lines", name = "START OF STANDARD DEVIATION 3"))
figure.add_trace(go.Scatter(x = [mathscore3stdDeviationEnd, mathscore3stdDeviationEnd], y = [0, 0.17], mode = "lines", name = "END OF STANDARD DEVIATION 3"))

figure.show()

#Printing the findings for Math score
DataWithinMath1stdDeviation = [result for result in mathscoreList if result > mathscore1stdDeviationStart and result < mathscore1stdDeviationEnd]
DataWithinMath2stdDeviation = [result for result in mathscoreList if result > mathscore2stdDeviationStart and result < mathscore2stdDeviationEnd]
DataWithinMath3stdDeviation = [result for result in mathscoreList if result > mathscore3stdDeviationStart and result < mathscore3stdDeviationEnd]

#Printing the findings for Reading score
DataWithinReading1stdDeviation = [result for result in readingscoreList if result > readingscore1stdDeviationStart and result < readingscore1stdDeviationEnd]
DataWithinReading2stdDeviation = [result for result in readingscoreList if result > readingscore2stdDeviationStart and result < readingscore2stdDeviationEnd]
DataWithinReading3stdDeviation= [result for result in readingscoreList if result > readingscore3stdDeviationStart and result < readingscore3stdDeviationEnd]

#Printing the findings for Writing score
DataWithinWriting1stdDeviation = [result for result in writingscoreList if result > writingscore1stdDeviationStart and result < writingscore1stdDeviationEnd]
DataWithinWriting2stdDeviation = [result for result in writingscoreList if result > writingscore2stdDeviationStart and result < writingscore2stdDeviationEnd]
DataWithinWriting3stdDeviation = [result for result in writingscoreList if result > writingscore3stdDeviationStart and result < writingscore3stdDeviationEnd]

#Math score
print("{} values of data lies within 1 standard Deviation(Math score)".format(len(DataWithinMath1stdDeviation)))
print("{}% of data lies within 1 standard Deviation(Math score)".format(len(DataWithinMath1stdDeviation)*100/len(mathscoreList)))

print("{} values of data lies within 2 standard Deviation(Math score)".format(len(DataWithinMath2stdDeviation)))
print("{}% of data lies within 2 standard Deviation(Math score)".format(len(DataWithinMath2stdDeviation)*100/len(mathscoreList)))

print("{} values of data lies within 3 standard Deviation(Math score)".format(len(DataWithinMath3stdDeviation)))
print("{}% of data lies within 3 standard Deviation(Math score)".format(len(DataWithinMath3stdDeviation)*100/len(mathscoreList)))

#Reading Score
print("{} values of data lies within 1 standard Deviation(Reading score)".format(len(DataWithinReading1stdDeviation)))
print("{}% of data lies within 1 standard Deviation(Reading score)".format(len(DataWithinReading1stdDeviation)*100/len(readingscoreList)))

print("{} values of data lies within 2 standard Deviation(Reading score)".format(len(DataWithinReading2stdDeviation)))
print("{}% of data lies within 2 standard Deviation(Reading score)".format(len(DataWithinReading2stdDeviation)*100/len(readingscoreList)))

print("{} values of data lies within 3 standard Deviation(Reading score)".format(len(DataWithinReading3stdDeviation)))
print("{}% of data lies within 3 standard Deviation(Reading score)".format(len(DataWithinReading3stdDeviation)*100/len(readingscoreList)))

#Writing Score
print("{} values of data lies within 1 standard Deviation(Writing score)".format(len(DataWithinWriting1stdDeviation)))
print("{}% of data lies within 1 standard Deviation(Writing score)".format(len(DataWithinWriting1stdDeviation)*100/len(writingscoreList)))

print("{} values of data lies within 2 standard Deviation(Writing score)".format(len(DataWithinWriting2stdDeviation)))
print("{}% of data lies within 2 standard Deviation(Writing score)".format(len(DataWithinWriting2stdDeviation)*100/len(writingscoreList)))

print("{} values of data lies within 3 standard Deviation(Writing score)".format(len(DataWithinWriting3stdDeviation)))
print("{}% of data lies within 3 standard Deviation(Writing score)".format(len(DataWithinWriting3stdDeviation)*100/len(writingscoreList)))