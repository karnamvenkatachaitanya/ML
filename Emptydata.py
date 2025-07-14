import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_values(file_path, method='mean'):
    df = pd.read_csv(file_path)
    columns_to_fill = ['Age', 'Marks']

    for col in columns_to_fill:
        if col in df.columns:
            if method == 'mean':
                df[col] = df[col].fillna(df[col].mean())
            elif method == 'median':
                df[col] = df[col].fillna(df[col].median())
            elif method == 'mode':
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                print(f"Unknown method: {method}")

    df['F/P'] = df['F/P'].map({'P': 1, 'F': 0})
    scaler = MinMaxScaler()
    df[['Age', 'Marks']] = scaler.fit_transform(df[['Age', 'Marks']])
    print(df)
fill_missing_values('/STUDENT.CSV', method='mean')
