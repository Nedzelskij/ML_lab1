import pandas as pd
from matplotlib import pyplot as plt


def print_number_rows_columns(df: pd.DataFrame):
    rows, columns = df.shape
    
    print(f'\nNumber of rows: {rows}')
    print(f'Number of columns: {columns}')


def print_K_rows(df: pd.DataFrame):
    K = 30
    print('\nOutput 5 records, starting with K-th last record:')
    print(df.loc[K : K + 4])

    mod_K = 3 * K + 2 
    print('Output 5 records, starting with 3K+2-th last record:')
    print(df.loc[mod_K : mod_K + 4])


def print_fields_types(df: pd.DataFrame):
    print("\nData types of each field:")
    print(df.dtypes)


def clean_text_spaces(text):
    if type(text) == str:
        return text.strip()
    

def clean_text_fields(df: pd.DataFrame):
    text_columns = df.select_dtypes(include='object').columns
    for column in text_columns:
        df[column] = df[column].apply(clean_text_spaces)


def convert_fields_to_numeric(df: pd.DataFrame):
        without_dollar_field = df['Career Earnings'].str.replace('$', '')
        without_percent_field = df['Winning Percentage'].str.replace('%', '')

        df['Career Earnings'] = pd.to_numeric(without_dollar_field)
        df['Winning Percentage'] = pd.to_numeric(without_percent_field)


def delete_empty_rows(df: pd.DataFrame):
    print('\nRows with empty fields')
    print(df[df.isnull().any(axis=1)])

    df.dropna(inplace=True)


def create_new_columns(df: pd.DataFrame):
    df['Win'] = df['Singles Record (Career)'].str.split('-').str[0].astype('Int64')
    df['Lose'] = df['Singles Record (Career)'].str.split('-').str[1].astype('Int64')
    df['Total'] = df['Win'] + df['Lose']


def delete_columns(df: pd.DataFrame, columns_for_delete):
    df.drop(columns=columns_for_delete, inplace=True)


def change_colums_order(df: pd.DataFrame):
    return df[['Rank', 'Name', 'Country', 'Pts', 'Total', 'Win', 'Lose', 'Winning Percentage', 'Career Earnings']]


def task_11(df: pd.DataFrame):
    print('\nTask 11.a:')
    df_2 = pd.DataFrame({'Unique Countries': df.sort_values(by='Country')['Country'].unique()})
    print(df_2)

    print('\nTask 11.b:')
    print(df.loc[df['Career Earnings'] == df['Career Earnings'].min(), ['Name', 'Pts']])

    print('\nTask 11.c:')
    print(df.loc[df['Win'] == df['Lose'], ['Name', 'Country']])


def task_12(df: pd.DataFrame):
    print('\nTask 12.a:')
    print(df['Country'].value_counts())

    print('\nTask 12.b:')
    print(df.groupby('Country')['Rank'].mean().reset_index())


def task_13(df: pd.DataFrame):
    df_2 = df.copy()
    df_2['Rank Group'] = ((df_2['Rank'] - 1) // 10 * 10).astype(str) + ' - ' + ((df_2['Rank'] - 1) // 10 * 10 + 10).astype(str)
    grouped_df_2 = df_2.groupby('Rank Group')['Lose'].sum()

    plt.figure(figsize=(10, 6))
    grouped_df_2.plot(kind='bar')
    plt.xlabel('Number of a group of 10 tennis players')
    plt.ylabel('Number of lost matches')
    plt.title('Number of lost matches in groups of 10, Top-100 rating')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def task_14(df: pd.DataFrame):
    total_prizes = df.groupby('Country')['Career Earnings'].sum()

    plt.figure(figsize=(10, 10))
    plt.pie(total_prizes, labels=total_prizes.index, autopct='%1.1f%%', startangle=90)
    plt.title('Total amount of prizes for each country')
    plt.tight_layout()
    plt.show()


def task_15(df: pd.DataFrame):
    average_number_points = df.groupby('Country')['Pts'].mean()
    average_number_matches_played = df.groupby('Country')['Total'].mean()

    plt.figure(figsize=(10, 6))
    plt.bar(average_number_points.index, average_number_points.values, label='Average number points')
    plt.bar(average_number_matches_played.index, average_number_matches_played.values, label='Average number played matches')

    plt.title('Average (number of matches, number of points) statistics by country')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    # task 1
    df = pd.read_csv('Top100-2007.csv')

    # task 2
    print_number_rows_columns(df)

    # task 3
    print_K_rows(df)

    # task 4
    print_fields_types(df)

    # task 5
    # print(df.head(5))
    clean_text_fields(df)
    # print(df.head(5))

    # task 6
    # print_fields_types(df)
    convert_fields_to_numeric(df)
    # print_fields_types(df)

    # task 7
    delete_empty_rows(df)

    # task 8
    create_new_columns(df)

    # task 9
    delete_columns(df, ['Singles Record (Career)', 'Link to Wikipedia'])

    # task 10
    df = change_colums_order(df)

    # task 11
    task_11(df)

    # task 12
    task_12(df)

    # task 13
    task_13(df)

    # task 14
    task_14(df)

    # task 15
    task_15(df)
    


if __name__ == '__main__':
    main()
