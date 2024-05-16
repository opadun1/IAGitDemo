import pandas as pd

data = {
    'FirstName': ["Artem", "Syed", "falcao"],
    'LastName': ["Frenk", "Shazli", "vaz"],
    'Year': ['Sophomore', 'Sophomore', 'unc']    
}
df = pd.DataFrame(data)
csv_name = "names.csv"
df.to_csv(csv_name, index = False)
print (f'Data saved to {csv_name}')