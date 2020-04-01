import pandas as pd
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('jeopardy.csv')

df.columns = df.columns.str.strip(' ')   #stripping the space from the column names
#print(df.columns)


def filter_strings(word_list):
    filtered_df = df[df.apply(lambda row: all([word in row['Question'] for word in word_list]), axis=1)]  #function to search for keywords in the question column

    return filtered_df

df['Question'] = df['Question'].str.lower()  #making the strings in the question column all lower case




#filtered_df = filter_strings(['king', 'england'])
#print(filtered_df.head())
#print("filtered_df.index: " + str(len(filtered_df.index)))

df['Value'] = df.Value.str.replace('\$', '')
df['Value'] = df.Value.str.replace(',', '')
df['Value'] = df.Value.str.replace('None', '0')
df['FinalQuestions'] = df.Value.isnull()

#print(df['FinalQuestions'])

df.Value = pd.to_numeric(df.Value)

#print(df['Value'])

filtered_df = filter_strings(['king'])
king_ave = filtered_df.Value.mean()

#print("the mean is: " + str(king_ave))

def get_answer_counts(data):
    return data["Answer"].value_counts()

print(get_answer_counts(filtered_df))

