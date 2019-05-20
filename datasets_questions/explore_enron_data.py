#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
#authors_file_handler = open(authors_file, "rb")
#    authors = pickle.load(authors_file_handler, fix_imports=True)

#enron = open("../final_project/final_project_dataset.pkl", "rb")
#enron_data = pickle.load(enron, fix_imports=True)
en = r'G:\udacity course git\ud120-projects\final_project\final_project_dataset_unix.pkl'
enron = open(en, "rb")
enron_data = pickle.load(enron,fix_imports=True)
print(len(enron_data))


