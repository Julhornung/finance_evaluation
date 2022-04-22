import pandas as pd


def get_column_names():

    """ reads the unstructured .names file and extracts the column names"""

    content_list =[]

    with open(r'../data/onehr.names') as f:
        for line in f:
            if ':' in line:
                content_list.append(line.split(':')[0])

    names_list = content_list[content_list.index('Date'):]

    names_list.append('ozone_day')

    return(names_list)

def get_data():
    
    names_list = get_column_names()

    df_data = pd.read_csv(r'../data/onehr.data', names = names_list, index_col=False)

    df_data['Date'] = pd.to_datetime(df_data['Date'])
    df_data['WSR0'] = pd.to_numeric(df_data['WSR0'], errors = 'coerce')

    # print(df_data.dtypes)

    return(df_data)

if __name__ == '__main__':
    get_data()