import pandas as pd 

states = ["California", "Texas", "Florida"]
#population = [39,28,22]

population = [163696,268597,170312]

dict_states = {"States":  states, "Population": population}

df_states = pd.DataFrame.from_dict(dict_states)

print(df_states)

df_states.to_csv('states.csv', index= False)



