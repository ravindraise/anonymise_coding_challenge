import os
import hashlib
import pandas as pd
import random
import string
from faker import Faker

columns = ['first_name', 'last_name', 'address', 'date_of_birth']
anonymize_columns = ['first_name', 'last_name', 'address']


# this function replaces sensitive data with random values
def randomize_values(df_ano, ano_fileds):
    for column in df_ano.columns:
        if column in ano_fileds:
            df_ano[column] = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in
                              range(len(df_ano))]  # generate a list of random strings
    return df_ano


# this function will encode the data using sha256 algorithm
def encode_sha256(x):
    return hashlib.sha256(x.encode()).hexdigest()


# generate data using fake library and create data frame returns it
def generate_csv(rows: int):
    fake = Faker('en_US')
    csv_rows = []
    for a in range(rows):
        row = [fake.first_name(), fake.last_name(), fake.address(), str(fake.date_of_birth())]
        csv_rows.append(row)
    df_input = pd.DataFrame(csv_rows, columns=columns)
    return df_input


# write data frame to csv file
def write_csv_file(df, csv_path: str):
    df.to_csv(csv_path, index=False, header=True)
    return csv_path


# this function will anonymize the input csv file using sha256 algorithm
def anonymize_sha256(input_df):
    df_sh256 = input_df
    for column in anonymize_columns:
        df_sh256[column] = df_sh256[column].apply(encode_sha256)
    return df_sh256


# this function will anonymize the input csv file with random values
def anonymize_random(input_df):
    df_rand = input_df
    df_rand = randomize_values(df_rand, anonymize_columns)
    return df_rand


# main method which will
# 1) generate the input data
# 2) Save the input data in to csv file in the current project directory
# 3) anonymize the csv file using sha256
# 4) anonymize the csv file random values
# 5) Save the anonymized csv files in the current project directory
def main(no_of_rows: int):
    # this function will generate the csv file
    input_df = generate_csv(no_of_rows)
    input_csv_file = os.getcwd() + os.sep + 'anonymize_input.csv'
    write_csv_file(input_df, input_csv_file)
    print("input csv  data file is : " + input_csv_file)
    print("input csv data is ")
    print(input_df.head())

    # this function will anonymize 'first_name', 'last_name', 'address' fields using sha256 algorithm
    df_sha256 = anonymize_sha256(input_df)

    # this function will write the anonymize csv file to the project current working directory
    output_file_sha256 = os.getcwd() + os.sep + 'anonymize_output_sha256.csv'
    write_csv_file(df_sha256, output_file_sha256)
    print("anonymize sha256 data file is : " + output_file_sha256)
    print("anonymize sha256 data is ")
    print(df_sha256.head())

    # this function will anonymize 'first_name', 'last_name', 'address' fields using random values
    df_random = anonymize_random(input_df)

    # this function will write the anonymize csv file to the project current working directory
    output_file_random = os.getcwd() + os.sep + 'anonymize_output_random.csv'
    write_csv_file(df_random, output_file_random)
    print("anonymize random data file is : " + output_file_random)
    print("anonymize random data is ")
    print(df_random.head())


# please pass the number of rows csv data to be generated for anonymize
if __name__ == "__main__":
    main(100)
