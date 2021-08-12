def load_and_process("https://github.com/data301-2021-summer2/group32-project/blob/main/data/raw/outbreaks.csv"):


    df1 = (
          pd.read_csv("https://github.com/data301-2021-summer2/group32-project/blob/main/data/raw/outbreaks.csv")
          .rename(processed_data)
          .dropna(axis = 0)
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)
    
replacement = {"January" : 1, "February":2,"March":3, "April" : 4, "May":5, "June":6,
               "July": 7, "August":8, "September":9,"October":10,"November":11,"December" :12,
               "Confirmed": 1,"Suspected": 0,"Confirmed; Confirmed" : 1,"Suspected; Suspected" : 0, "Confirmed; Confirmed; Confirmed" : 1, 
               "Confirmed; Confirmed; Confirmed; Confirmed; Confirmed; Confirmed" : 1, "Suspected; Confirmed; Confirmed" : 0,
               "Suspected; Suspected; Confirmed; Suspected; Suspected; Confirmed" : 0, "Confirmed; Confirmed; Confirmed; Confirmed; Confirmed; Confirmed" : 1,
        
               "Suspected; Confirmed" : 0, "Confirmed; Suspected" : 0, "Fast Food Restaurant" : 0, "Restaurant":0,
               "Catering Service" : 0, "Religious Facility" : 0, "Grocery Store" : 0, "Prison/Jail" : 0, "Fair/Festival" : 0,
               "Private Home/Residence" : 1, "Camp": 1, "School/College/University" :1, "Nursing Home/Assisted Living Facility" : 1,
               "Unknown" : 1, "Private Home/Restuarant; Religious Facility" : 2, "Private Home/Restuarant; Grocery Store" : 2, 
               "Restaurant; Private Home/Residence": 0, "Private Home/Residence; Catering Service" : 0, 
               "Restaurant; Nursing Home/Assisted Living Facility" : 0, "Restaurant; Grocery Store": 0,
               "Restaurant; Catering Service":0, "Private Home/Residence; Banquet Facility" : 0, "Restaurant; Banquet Facility" : 0,
               "Restaurant Buffet" :0,"Banquet Facility" :0, "Restaurant; School/College/University":0,"Salmonella enterica" : 0, 
               "Salmonella enterica; Salmonella enterica" : 0, "Norovirus genogroup I; Norovirus genogroup II" : 2, "Norovirus genogroup I": 2,
                "Escherichia coli, Shiga toxin-producing" : 1, "Norovirus genogroup II" : 2}

    processed_data = (
          df1
          .assign(replacement)
      )


    return processed_data 

