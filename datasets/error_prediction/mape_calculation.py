import csv
import numpy as np

def read_file(filename, char_delimiter):
    with open(filename) as csv_file:
        y_pred = []
        y_true = []
        y_diff = []
        csv_reader = csv.reader(csv_file, delimiter=char_delimiter)
        #Jump first line
        next(csv_reader, None)
        for row in csv_reader:
            y_true.append(float(row[1]))
            y_pred.append(float(row[2]))
            y_diff.append(abs(float(row[3])))

    return y_true, y_pred, y_diff

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


models = ['LR', 'RN', 'RR', 'MLP', 'SMOreg','Ibk','LWL','DT', 'M5P', 'RT']
apps = ['bitcount', 'cjpeg', 'crc32', 'FFT', 'gsmdec', 'sha']

print(*models, sep = ", ")
for app in apps:
    r_models = []
    for ml in models:
        y_true, y_pred, y_diff = read_file(ml+'_'+app+'_error.csv', ',')
        mape = mean_absolute_percentage_error(y_true, y_pred)
        r_models.append(mape)
    print(app, *r_models, sep= ", ")
