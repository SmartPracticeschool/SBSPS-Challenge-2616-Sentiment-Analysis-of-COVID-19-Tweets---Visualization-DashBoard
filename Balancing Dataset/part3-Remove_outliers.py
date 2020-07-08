def remove_outliers(df):
    for col in df.columns:
        '''We are using an inter quantile range of 0.05 to 0.95'''
        '''The columns which are having outliers are neglected else they are taken'''
        if (((df[col].dtype)=='float64') | ((df[col].dtype)=='int64')):
            ''' The percentiles values contain the range values for 0.05 and 0.95'''
            percentiles_values = df[col].quantile([0.05,0.95]).values
            df[col][df[col] <= percentiles_values[0]] = percentiles_values[0]
            df[col][df[col] >= percentiles_values[1]] = percentiles_values[1]
        else:
            df[col]=df[col]
    return df

final_df=remove_outliers(df1)
