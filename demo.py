import pandas as pd

data = {

    'FirstName': ["Artem", "Syed", "falcao","Oleksii"],
    'LastName': ["Frenk", "Shazli", "vaz", "Padun"],
    'Year': ['Sophomore', 'Sophomore', 'unc', 'PhD 2']    

}
df = pd.DataFrame(data)
csv_name = "names.csv"
df.to_csv(csv_name, index = False)
print (f'Data saved to {csv_name}')