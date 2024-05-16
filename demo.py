import pandas as pd

data = {
    'FirstName': ["Artem"],
    'LastName': ["Frenk"],
    'Year': ['Sophomore']    

}
df = pd.DataFrame(data)
csv_name = "names.csv"
df.to_csv(csv_name, index = False)
print (f'Data saved to {csv_name}')