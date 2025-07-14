import pandas as pd

def fill_missing_values(file_path, method):
    df = pd.read_csv(file_path)

    if method == 'mean':
        df['Age'] = df['Age'].fillna(df['Age'].mean())
        df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
    elif method == 'median':
        df['Age'] = df['Age'].fillna(df['Age'].median())
        df['Marks'] = df['Marks'].fillna(df['Marks'].median())
    elif method == 'mode':
        df['Age'] = df['Age'].fillna(df['Age'].mode()[0])
        df['Marks'] = df['Marks'].fillna(df['Marks'].mode()[0])

    print(df)

fill_missing_values('/STUDENT.CSV', 'mean')
