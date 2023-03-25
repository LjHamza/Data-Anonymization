import pandas as pd


df_anon = pd.read_csv('hamza_anony2.csv')
df_original = pd.read_csv('data_init.csv')

def charges():
    
    # Recreating playground dataframe with only relevant values (charges in both anonymized and original data)
    df = pd.DataFrame({
        'df_anonymized_charges': df_anon['charges'],
        'df_origin_charges': df_original['charges']
    })


    #if the charges column is of list type,as in the cas of k-anonymity.
    """
    if type(df['df_anonymized_charges'][0])==list:
       
        average_charges=[]
        for i in df['df_anonymized_charges']:
            avg = sum(i[0])/2
            average_charges.append(avg)
    
        df = pd.DataFrame({
            'df_anonymized_charges': average_charges,
            'df_origin_charges': df_original['charges']
        })
        

    """
    
    #Calculating the percentage of anonymized charges on original charges
    df['difference']=abs(df['df_anonymized_charges']-df['df_origin_charges'])
    
    df['ratio'] = (df['difference']/df['df_origin_charges'])*10
    for i in range(len(df['ratio'])):
        if df['ratio'][i] >=1:
           df['ratio'][i]=1
    
    # Creating score
    df['score'] = 1 - df['ratio']
    score = df['score'].sum()
    score = df['score'].sum()

    score=score/len(df['score'])

    return score


def correlation():

    
    corr_original=df_original.corr(numeric_only=True)
    corr_anon=df_anon.corr(numeric_only=True)

    
    diff=(abs(corr_original-corr_anon)-0)/(2-0) #normlizing the result because the abs(diff) will be in a range between 0 and 2.

    result=diff.sum()
    score=0
    
    for i in result:
        score=score+i
   
    score=1-(score/16)

    return score    


    
def distribution():


    original_sex_dist=df_original['sex'].value_counts()
    ano_sex_dist=df_anon['sex'].value_counts()

    original_smoker_dist=df_original['smoker'].value_counts()
    ano_smoker_dist=df_anon['smoker'].value_counts()
    
    diff_sex_dist=original_sex_dist-ano_sex_dist
    diff_smoker_dist=original_smoker_dist-ano_smoker_dist

    result=abs(diff_sex_dist[0])+abs(diff_sex_dist[1])+abs(diff_smoker_dist[0])+abs(diff_smoker_dist[1])

    if result>30:
        score=0
    else:
        result=result/30
    
    score=1-result

    return score



def score():
    first_score=charges()
    second_score=correlation()
    third_score=distribution()

    score=(first_score+second_score+third_score)/3

    
    print(score)

   
score()