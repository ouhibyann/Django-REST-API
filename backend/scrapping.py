""" As asked, this is a script to scrap and send to the database.
    It is not part of the web based application
"""

from pandas import read_csv, concat
from sqlalchemy import create_engine

# Reading the csv and concatenating them
pd1 = read_csv(r"./data/208.csv")
pd2 = read_csv(r"./data/270.csv")

data = concat([pd1, pd2])

# Sending the dataframe to the database
engine = create_engine('postgresql://postgres:postgres@db:5432/UPciti', echo=True)
data.to_sql('Tower',
            engine,
            if_exists='replace')  # replace ensure that we do not duplicate data
